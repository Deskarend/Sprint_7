import allure
import requests
from endpoints.base_point import BasePoint


class GetOrderList(BasePoint):
    GET_ORDER_LIST_ENDPOINT = '/api/v1/orders'

    STATUS_CODE_OF_SUCCESSFUL_GET_ORDER_LIST = 200

    @allure.step('Получение списка заказов')
    def get_order_list(self):
        url = self.BASE_URL + self.GET_ORDER_LIST_ENDPOINT
        self.response = requests.get(url)
        self.response_json = self.response.json()

    @allure.step('Проверка статус кода получения списка заказов')
    def check_response_status_code_of_successful_getting_order_list(self):
        self.check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_GET_ORDER_LIST)

    @allure.step('Проверка тела ответа списка заказов')
    def check_response_body_of_getting_order_list(self):
        assert type(self.response_json['orders']) is list and len(self.response_json['orders']) > 0

    @allure.step('Проверка ответа получения списка заказов')
    def check_response_getting_order_list(self):
        self.check_response_status_code_of_successful_getting_order_list()
        self.check_response_body_of_getting_order_list()
