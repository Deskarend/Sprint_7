import allure
import requests
from endpoints.base_point import BasePoint


class LoginCourier(BasePoint):
    LOGIN_COURIER_ENDPOINT = '/api/v1/courier/login'
    STATUS_CODE_OF_SUCCESSFUL_LOGIN = 200

    STATUS_CODE_OF_LOGIN_WITHOUT_LOGIN = 400
    RESPONSE_MESSAGE_OF_LOGIN_WITHOUT_LOGIN = 'Недостаточно данных для входа'

    STATUS_CODE_OF_LOGIN_WITH_NOT_EXISTING_COURIER = 404
    RESPONSE_MESSAGE_OF_LOGIN_WITH_NOT_EXISTING_COURIER = 'Учетная запись не найдена'

    @allure.step('Авторизация курьера')
    def login_courier(self, payload):
        url = self.BASE_URL + self.LOGIN_COURIER_ENDPOINT
        self.response = requests.post(url, json=payload)
        self.response_json = self.response.json()

    @allure.step('Получение id курьера')
    def get_id_courier(self):
        return self.response_json.get('id')

    @allure.step('Проверка статус кода успешной авторизации')
    def check_response_status_code_of_successful_login(self):
        self.check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_LOGIN)

    @allure.step('Проверка тела ответа успешной авторизации')
    def check_response_body_of_successful_login(self):
        assert self.response_json.get('id', False), 'В теле ответа нет id'

    @allure.step('Проверка ответа успешной авторизации')
    def check_response_of_successful_login(self):
        self.check_response_status_code_of_successful_login()
        self.check_response_body_of_successful_login()

    @allure.step('Проверка статус кода авторизации c невалидным телом')
    def check_response_status_code_of_login_with_invalid_body(self):
        self.check_response_status_code(self.STATUS_CODE_OF_LOGIN_WITHOUT_LOGIN)

    @allure.step('Проверка сообщения в теле ответа авторизации с невалидным телом')
    def check_response_message_of_login_with_invalid_body(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_LOGIN_WITHOUT_LOGIN)

    @allure.step('Проверка ответа авторизации с невалидным телом')
    def check_response_of_login_with_invalid_body(self):
        self.check_response_status_code_of_login_with_invalid_body()
        self.check_response_message_of_login_with_invalid_body()

    @allure.step('Проверка авторизации c неправильным логином или паролем')
    def check_response_status_code_with_incorrect_login_or_password(self):
        self.check_response_status_code(self.STATUS_CODE_OF_LOGIN_WITH_NOT_EXISTING_COURIER)

    @allure.step('Проверка сообщения в теле ответа авторизации с неправильным логином или паролем')
    def check_response_message_with_incorrect_login_or_password(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_LOGIN_WITH_NOT_EXISTING_COURIER)

    @allure.step('Проверка ответа авторизации с неправильным логином или паролем')
    def check_response_with_incorrect_login_or_password(self):
        self.check_response_status_code_with_incorrect_login_or_password()
        self.check_response_message_with_incorrect_login_or_password()
