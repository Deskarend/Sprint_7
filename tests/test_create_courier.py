import allure
import pytest
from endpoints.base_point import BasePoint
from endpoints.create_courier import CreateCourier


class TestCreateCourier:
    @allure.title('Проверка создания курьера')
    @allure.description('При успешном создании курьера код ответа: 201, тело ответа: {"ok": True}')
    def test_create_new_courier(self, payload_for_new_courier):
        create_courier = CreateCourier()

        create_courier.create_courier(payload_for_new_courier)

        create_courier.check_response_of_successful_create_courier()

    @allure.title('Проверка создания двух одинаковых курьера')
    @allure.description('При создании двух одинаковых курьера код ответа: 409, сообщение в теле : "Этот логин '
                        'уже используется. Попробуйте другой."')
    def test_create_two_identical_couriers(self, payload_for_new_courier):
        create_courier = CreateCourier()

        create_courier.create_courier(payload_for_new_courier)
        create_courier.create_courier(payload_for_new_courier)

        create_courier.check_response_of_create_courier_with_existing_login()

    @allure.title('Проверка создания курьеров с одинаковыми логинами')
    @allure.description('При создании курьеров с одинаковыми логинами код ответа: 409, сообщение в теле : '
                        '"Этот логин уже используется. Попробуйте другой."')
    def test_create_two_identical_logins(self, payload_for_new_courier):
        create_courier = CreateCourier()

        create_courier.create_courier(payload_for_new_courier)

        new_payload = create_courier.regenerate_password_and_name(payload_for_new_courier)
        create_courier.create_courier(new_payload)

        create_courier.check_response_of_create_courier_with_existing_login()

    @allure.title('Проверка создания курьеров без передачи всех обязательный полей')
    @allure.description('При создании курьера без передачи всех обязательный полей код ответа: 400, '
                        'сообщение в теле : "Недостаточно данных для создания учетной записи"')
    @pytest.mark.parametrize('generate_invalid_payload', [BasePoint.generate_payload_without_login,
                                                          BasePoint.generate_payload_without_password,
                                                          BasePoint.generate_payload_without_login_and_password])
    def test_create_courier_without_required_parameter(self, generate_invalid_payload):
        create_courier = CreateCourier()
        payload = generate_invalid_payload()

        create_courier.create_courier(payload)

        create_courier.check_response_of_create_courier_with_invalid_body()
