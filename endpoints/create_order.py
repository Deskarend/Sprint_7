import allure
import requests
from endpoints.base_point import BasePoint


class CreateOrder(BasePoint):
    CREATE_ORDER_ENDPOINT = '/api/v1/orders'

    STATUS_CODE_OF_SUCCESSFUL_CREATE_ORDER = 201

    def create_order(self, payload):
        url = self.BASE_URL + self.CREATE_ORDER_ENDPOINT
        self.response = requests.post(url, json=payload)
        self.response_json = self.response.json()

    def get_order_track(self):
        return self.response_json.get('track')

    @allure.step('Проверка статус кода успешного создания заказа')
    def check_response_status_code_of_successful_create_order(self):
        self.check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_CREATE_ORDER)

    @allure.step('Проверка тела ответа успешного создания заказа')
    def check_response_body_of_successful_create_oder(self):
        assert self.response_json.get('track'), 'В теле ответа нет track'

    @allure.step('Проверка ответа успешного создания заказа')
    def check_response_successful_create_order(self):
        self.check_response_status_code_of_successful_create_order()
        self.check_response_body_of_successful_create_oder()

    @staticmethod
    def add_color(payload, color):
        if type(color) is list:
            payload['color'].extend(color)
        else:
            payload['color'].append(color)
