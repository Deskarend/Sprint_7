import random
import allure
from data import generate_random_string


class BasePoint:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    response = None
    response_json = None

    def check_response_status_code(self, status_code):
        assert self.response.status_code == status_code, (f'Ожидаемый код ответа:{status_code}, '
                                                          f'фактический:{self.response.status_code}')

    def check_response_body(self, response_body):
        assert self.response_json == response_body, (f'Ожидаемое тело ответа:{response_body}, '
                                                     f'фактическое :{self.response_json}')

    def check_response_message(self, message):
        assert self.response_json['message'] == message, (f"Ожидаемый текст ошибки:'{message}', фактический "
                                                          f"'{self.response_json['message']}'")

    @staticmethod
    @allure.step('Изменение пароля и имени в теле запроса на создание курьера')
    def regenerate_password_and_name(payload):
        new_payload = payload.copy()

        new_payload["password"] = generate_random_string(10)
        new_payload["firstName"] = generate_random_string(10)

        return new_payload

    @staticmethod
    @allure.step('Генерация тела запроса без логина на создании курьера')
    def generate_payload_without_login():
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "password": password,
            "firstName": first_name
        }

        return payload

    @staticmethod
    @allure.step('Генерация тела запроса без пароля на создании курьера')
    def generate_payload_without_password():
        login = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "firstName": first_name
        }

        return payload

    @staticmethod
    @allure.step('Генерация тела запроса без логина и пароля на создании курьера')
    def generate_payload_without_login_and_password():
        first_name = generate_random_string(10)

        payload = {
            "firstName": first_name
        }

        return payload

    @staticmethod
    @allure.step('Удаление логина в теле запроса при авторизации')
    def delete_login_from_payload(payload):
        new_payload = payload.copy()
        new_payload['login'] = ''
        return new_payload

    @staticmethod
    @allure.step('Удаление пароля в теле запроса при авторизации')
    def delete_password_from_payload(payload):
        new_payload = payload.copy()
        new_payload['password'] = ''
        return new_payload

    @staticmethod
    @allure.step('Удаление пароля и логина в теле запроса при авторизации')
    def delete_login_and_password_from_payload(payload):
        new_payload = payload.copy()
        new_payload = BasePoint.delete_login_from_payload(new_payload)
        new_payload = BasePoint.delete_password_from_payload(new_payload)
        return new_payload

    @staticmethod
    @allure.step('Изменение пароля в теле запроса на авторизацию курьера')
    def regenerate_password(payload):
        new_payload = payload.copy()
        new_payload["password"] = generate_random_string(10)
        return new_payload

    @staticmethod
    @allure.step('Изменение логина в теле запроса на авторизацию курьера')
    def regenerate_login(payload):
        new_payload = payload.copy()
        new_payload["login"] = generate_random_string(10)
        return new_payload

    @staticmethod
    @allure.step('Генерирование случайного id')
    def generate_random_id():
        return random.randint(1000000, 999999999)
