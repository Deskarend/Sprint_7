import allure
import requests
from endpoints.base_point import BasePoint


class CreateCourier(BasePoint):
    CREATE_ENDPOINT = '/api/v1/courier'

    STATUS_CODE_OF_SUCCESSFUL_CREATE_COURIER = 201
    RESPONSE_BODY_OF_SUCCESSFUL_CREATE_COURIER = {"ok": True}

    STATUS_CODE_OF_CREATE_COURIER_WITH_EXISTING_LOGIN = 409
    RESPONSE_MESSAGE_OF_CREATE_COURIER_WITH_EXISTING_LOGIN = 'Этот логин уже используется'

    STATUS_CODE_OF_CREATE_COURIER_WITH_INVALID_BODY = 400
    RESPONSE_MESSAGE_OF_CREATE_COURIER_WITH_INVALID_BODY = 'Недостаточно данных для создания учетной записи'

    @allure.step('Создание курьера')
    def create_courier(self, payload):
        url = self.BASE_URL + self.CREATE_ENDPOINT
        self.response = requests.post(url, data=payload)
        self.response_json = self.response.json()

    @allure.step('Проверка статус кода успешного создания курьера')
    def check_response_status_code_of_successful_create_courier(self):
        self.check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_CREATE_COURIER)

    @allure.step('Проверка тела ответа успешного создания курьера')
    def check_response_body_of_successful_create_courier(self):
        self.check_response_body(self.RESPONSE_BODY_OF_SUCCESSFUL_CREATE_COURIER)

    @allure.step('Проверка ответа успешного создания курьера')
    def check_response_of_successful_create_courier(self):
        self.check_response_status_code_of_successful_create_courier()
        self.check_response_body_of_successful_create_courier()

    @allure.step('Проверка статус кода запроса создания курьера с существующим логином')
    def check_response_status_code_of_create_courier_with_existing_login(self):
        self.check_response_status_code(self.STATUS_CODE_OF_CREATE_COURIER_WITH_EXISTING_LOGIN)

    @allure.step('Проверка сообщения в теле ответа создания курьера с существующим логином')
    def check_response_message_of_create_courier_with_existing_login(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_CREATE_COURIER_WITH_EXISTING_LOGIN)

    @allure.step('Проверка ответа создания курьера с существующим логином')
    def check_response_of_create_courier_with_existing_login(self):
        self.check_response_status_code_of_create_courier_with_existing_login()
        self.check_response_message_of_create_courier_with_existing_login()

    @allure.step('Проверка статус кода создания курьера с невалидным телом')
    def check_response_status_code_of_create_courier_with_invalid_body(self):
        self.check_response_status_code(self.STATUS_CODE_OF_CREATE_COURIER_WITH_INVALID_BODY)

    @allure.step('Проверка сообщения в теле ответа создания курьера с невалидным телом')
    def check_response_message_of_create_courier_with_invalid_body(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_CREATE_COURIER_WITH_INVALID_BODY)

    @allure.step('Проверка ответа создания курьера с невалидным телом')
    def check_response_of_create_courier_with_invalid_body(self):
        self.check_response_status_code_of_create_courier_with_invalid_body()
        self.check_response_message_of_create_courier_with_invalid_body()
