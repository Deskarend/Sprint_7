import allure
import requests
from endpoints.base_point import BasePoint


class GetOrderByTrack(BasePoint):
    GET_ORDER_BY_TRACK_ENDPOINT = '/api/v1/orders/track'
    PARAMETER_NAME = 't'

    STATUS_CODE_OF_SUCCESSFUL_GET_ORDER_BY_TRACK = 200

    STATUS_CODE_OF_GET_ORDER_BY_TRACK_WITHOUT_TRACK = 400
    RESPONSE_MESSAGE_OF_GETTING_ORDER_BY_TRACK_WITHOUT_TRACK = 'Недостаточно данных для поиска'

    STATUS_CODE_OF_GET_ORDER_BY_TRACK_WITH_NOT_EXISTING_ORDER = 404
    RESPONSE_MESSAGE_OF_GETTING_ORDER_BY_TRACK_WITH_NOT_EXISTING_ORDER = 'Заказ не найден'

    @allure.step('Получение заказа по его трекинговому номеру')
    def get_order_by_track(self, track=None):
        url = self.BASE_URL + self.GET_ORDER_BY_TRACK_ENDPOINT

        if track:
            query_params = f'?{self.PARAMETER_NAME}={str(track)}'
            url += query_params

        self.response = requests.get(url)
        self.response_json = self.response.json()

    @allure.step('Получение id заказа')
    def get_order_id(self):
        return self.response_json['order'].get('id')

    @allure.step('Проверка статус кода успешного получения заказа по его трекинговому номеру')
    def check_response_status_code_of_successful_getting_order_by_track(self):
        self.check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_GET_ORDER_BY_TRACK)

    @allure.step('Проверка тела ответа успешного полученного заказа по его трекинговому номеру')
    def check_response_body_of_getting_order_by_track(self):
        assert self.response_json.get('order'), 'В теле заказа отсутствует объект с заказом  или объект заказа пуст'

    @allure.step('Проверка ответа успешного получения заказа по его трекинговому номеру')
    def check_response_successful_getting_order_by_track(self):
        self.check_response_status_code_of_successful_getting_order_by_track()
        self.check_response_body_of_getting_order_by_track()

    @allure.step('Проверка статус кода получения заказа по его трекинговому номеру без номера')
    def check_response_status_code_of_getting_order_by_track_without_track(self):
        self.check_response_status_code(self.STATUS_CODE_OF_GET_ORDER_BY_TRACK_WITHOUT_TRACK)

    @allure.step('Проверка тела ответа полученного заказа по его трекинговому номеру без номера')
    def check_response_body_of_getting_order_by_track_without_track(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_GETTING_ORDER_BY_TRACK_WITHOUT_TRACK)

    @allure.step('Проверка ответа получения заказа по его трекинговому номеру без номера')
    def check_response_getting_order_by_track_without_track(self):
        self.check_response_status_code_of_getting_order_by_track_without_track()
        self.check_response_body_of_getting_order_by_track_without_track()

    @allure.step('Проверка статус кода получения заказа по его трекинговому номеру с несуществующим номером')
    def check_response_status_code_of_getting_order_by_track_with_not_existing_track(self):
        self.check_response_status_code(self.STATUS_CODE_OF_GET_ORDER_BY_TRACK_WITH_NOT_EXISTING_ORDER)

    @allure.step('Проверка тела ответа полученного заказа по его трекинговому номеру с несуществующим номером')
    def check_response_body_of_getting_order_by_track_with_not_existing_track(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_GETTING_ORDER_BY_TRACK_WITH_NOT_EXISTING_ORDER)

    @allure.step('Проверка ответа получения заказа по его трекинговому номеру с несуществующим номером')
    def check_response_getting_order_by_track_with_not_existing_track(self):
        self.check_response_status_code_of_getting_order_by_track_with_not_existing_track()
        self.check_response_body_of_getting_order_by_track_with_not_existing_track()