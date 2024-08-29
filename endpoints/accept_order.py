import allure
import requests
from endpoints.base_point import BasePoint


class AcceptOrder(BasePoint):
    ACCEPT_ORDER_ENDPOINT = '/api/v1/orders/accept/'
    PARAMETER_NAME_OF_COURIER_ID = 'courierId'

    STATUS_CODE_OF_SUCCESSFUL_ACCEPT_ORDER = 200
    RESPONSE_BODY_OF_SUCCESSFUL_ACCEPT_ORDER = {"ok": True}

    STATUS_CODE_OF_ACCEPT_ORDER_WITHOUT_ORDER_OR_COURIER_ID = 400
    RESPONSE_MESSAGE_OF_ACCEPT_ORDER_WITHOUT_ORDER_OR_COURIER_ID = 'Недостаточно данных для поиска'

    STATUS_CODE_OF_ACCEPT_ORDER_WITH_NOT_EXISTING_ORDER_OR_COURIER_ID = 404
    RESPONSE_MESSAGE_OF_ACCEPT_ORDER_WITH_NOT_EXISTING_ORDER_ID = 'Заказа с таким id не существует'
    RESPONSE_MESSAGE_OF_ACCEPT_ORDER_WITH_NOT_EXISTING_COURIER_ID = 'Курьера с таким id не существует'

    @allure.step('Принять заказ')
    def accept_order(self, order_id=None, courier_id=None):
        url = self.BASE_URL + self.ACCEPT_ORDER_ENDPOINT

        if order_id:
            url += str(order_id)
        if courier_id:
            query_params = f'?{self.PARAMETER_NAME_OF_COURIER_ID}={courier_id}'
            url += query_params

        self.response = requests.put(url)
        self.response_json = self.response.json()

    @allure.step('Проверка статус кода успешного принятия заказа')
    def check_response_status_code_of_successful_accept_order(self):
        self.check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_ACCEPT_ORDER)

    @allure.step('Проверка тела ответа успешного принятия заказа')
    def check_response_body_of_successful_accept_order(self):
        self.check_response_body(self.RESPONSE_BODY_OF_SUCCESSFUL_ACCEPT_ORDER)

    @allure.step('Проверка ответа успешного принятия заказа')
    def check_response_of_successful_accept_order(self):
        self.check_response_status_code_of_successful_accept_order()
        self.check_response_body_of_successful_accept_order()

    @allure.step('Проверка статус кода принятия заказа без id курьера')
    def check_response_status_code_of_accept_order_without_courier_or_order_id(self):
        self.check_response_status_code(self.STATUS_CODE_OF_ACCEPT_ORDER_WITHOUT_ORDER_OR_COURIER_ID)

    @allure.step('Проверка тела ответа принятия заказа без id курьера')
    def check_response_message_of_accept_order_without_courier_id(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_ACCEPT_ORDER_WITHOUT_ORDER_OR_COURIER_ID)

    @allure.step('Проверка ответа принятия заказа без id курьера')
    def check_response_of_accept_order_without_courier_id(self):
        self.check_response_status_code_of_accept_order_without_courier_or_order_id()
        self.check_response_message_of_accept_order_without_courier_id()

    @allure.step('Проверка статус кода принятия заказа c несуществующим id курьера или заказа')
    def check_response_status_code_of_accept_order_with_not_existing_courier_or_order_id(self):
        self.check_response_status_code(self.STATUS_CODE_OF_ACCEPT_ORDER_WITH_NOT_EXISTING_ORDER_OR_COURIER_ID)

    @allure.step('Проверка тела ответа принятия заказа c несуществующим id курьера')
    def check_response_message_of_accept_order_with_not_existing_courier_id(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_ACCEPT_ORDER_WITH_NOT_EXISTING_COURIER_ID)

    @allure.step('Проверка ответа принятия заказа c несуществующим id курьера')
    def check_response_of_accept_order_with_not_existing_courier_id(self):
        self.check_response_status_code_of_accept_order_with_not_existing_courier_or_order_id()
        self.check_response_message_of_accept_order_with_not_existing_courier_id()

    @allure.step('Проверка тела ответа принятия заказа c несуществующим id заказа')
    def check_response_message_of_accept_order_with_not_existing_order_id(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_ACCEPT_ORDER_WITH_NOT_EXISTING_ORDER_ID)

    @allure.step('Проверка ответа принятия заказа c несуществующим id курьера')
    def check_response_of_accept_order_with_not_existing_order_id(self):
        self.check_response_status_code_of_accept_order_with_not_existing_courier_or_order_id()
        self.check_response_message_of_accept_order_with_not_existing_order_id()
