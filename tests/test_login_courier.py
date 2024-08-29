import allure
import pytest
from endpoints.base_point import BasePoint
from endpoints.login_courier import LoginCourier


class TestLoginCourier:
    @allure.title('Проверка авторизации курьера')
    @allure.description('При успешной авторизации курьера код ответа: 200, в теле ответа содержится id')
    def test_login_courier(self, login_and_password_of_new_courier):
        login_courier = LoginCourier()

        login_courier.login_courier(login_and_password_of_new_courier)

        login_courier.check_response_of_successful_login()

    @allure.title('Проверка авторизации курьеров без передачи обязательных полей')
    @allure.description('При авторизации курьера без передачи обязательных полей код ответа: 400 , '
                        'в теле ответа сообщение: "Недостаточно данных для входа"')
    @pytest.mark.parametrize('generate_invalid_payload', [BasePoint.delete_login_from_payload,
                                                          BasePoint.delete_password_from_payload,
                                                          BasePoint.delete_login_and_password_from_payload])
    def test_login_courier_without_password_and_login(self, login_and_password_of_new_courier,
                                                      generate_invalid_payload):
        login_courier = LoginCourier()
        invalid_payload = generate_invalid_payload(login_and_password_of_new_courier)

        login_courier.login_courier(invalid_payload)

        login_courier.check_response_of_login_with_invalid_body()

    @allure.title('Проверка авторизации курьера с неправильны паролем или логином')
    @allure.description('При авторизации курьера с неправильным паролем или логином код ответа: 404, '
                        'в теле ответа сообщение: "Учетная запись не найдена" ')
    @pytest.mark.parametrize('generate_incorrect_payload', [BasePoint.regenerate_password,
                                                            BasePoint.regenerate_login])
    def test_login_courier_with_incorrect_password_or_login(self, login_and_password_of_new_courier,
                                                            generate_incorrect_payload):
        login_courier = LoginCourier()
        incorrect_payload = generate_incorrect_payload(login_and_password_of_new_courier)

        login_courier.login_courier(incorrect_payload)

        login_courier.check_response_with_incorrect_login_or_password()

    @allure.title('Проверка авторизации несуществующего курьера')
    @allure.description('При авторизации несуществующего курьера  код ответа: 404, '
                        'в теле ответа сообщение: "Учетная запись не найдена" ')
    def test_login_courier_with_not_existing_courier(self, payload_for_new_courier):
        login_courier = LoginCourier()

        login_courier.login_courier(payload_for_new_courier)

        login_courier.check_response_with_incorrect_login_or_password()
