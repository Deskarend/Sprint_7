import allure
import requests
from endpoints.base_point import BasePoint


class DeleteCourier(BasePoint):
    DELETE_COURIER_ENDPOINT = '/api/v1/courier/'

    STATUS_CODE_OF_SUCCESSFUL_DELETE = 200
    RESPONSE_BODY_OF_SUCCESSFUL_DELETE = {'ok': True}

    STATUS_CODE_OF_DELETE_WITHOUT_ID = 400
    RESPONSE_MESSAGE_OF_DELETE_WITHOUT_ID = 'Недостаточно данных для удаления курьера'

    STATUS_CODE_OF_DELETE_WITH_NOT_EXISTING_ID = 404
    RESPONSE_MESSAGE_OF_DELETE_WITH_NOT_EXISTING = 'Курьера с таким id нет'

    @allure.step('Удаление курьера')
    def delete_courier(self, courier_id=None):
        if courier_id:
            url = self.BASE_URL + self.DELETE_COURIER_ENDPOINT + str(courier_id)
        else:
            url = self.BASE_URL + self.DELETE_COURIER_ENDPOINT
        self.response = requests.delete(url)
        self.response_json = self.response.json()

    @allure.step('Проверка статус кода успешного удаления курьера')
    def check_response_status_code_of_successful_delete_courier(self):
        self.check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_DELETE)

    @allure.step('Проверка тела ответа успешного удаления курьера')
    def check_response_body_of_successful_delete(self):
        self.check_response_body(self.RESPONSE_BODY_OF_SUCCESSFUL_DELETE)

    @allure.step('Проверка ответа успешного удаления курьера')
    def check_response_of_successful_delete(self):
        self.check_response_status_code_of_successful_delete_courier()
        self.check_response_body_of_successful_delete()

    @allure.step('Проверка статус кода удаления курьера c несуществующим id')
    def check_response_status_code_of_delete_courier_with_not_existing_id(self):
        self.check_response_status_code(self.STATUS_CODE_OF_DELETE_WITH_NOT_EXISTING_ID)

    @allure.step('Проверка тела ответа удаления курьера c несуществующим id')
    def check_response_message_of_delete_courier_with_not_existing_id(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_DELETE_WITH_NOT_EXISTING)

    @allure.step('Проверка ответа удаления курьера c несуществующим id')
    def check_response_of_delete_courier_with_not_existing_id(self):
        self.check_response_status_code_of_delete_courier_with_not_existing_id()
        self.check_response_message_of_delete_courier_with_not_existing_id()

    @allure.step('Проверка статус кода удаления курьера без id')
    def check_response_status_code_of_delete_courier_without_id(self):
        self.check_response_status_code(self.STATUS_CODE_OF_DELETE_WITHOUT_ID)

    @allure.step('Проверка тела ответа удаления курьера без id')
    def check_response_message_of_delete_courier_without_id(self):
        self.check_response_message(self.RESPONSE_MESSAGE_OF_DELETE_WITHOUT_ID)

    @allure.step('Проверка ответа удаления курьера без id')
    def check_response_of_delete_courier_without_id(self):
        self.check_response_status_code_of_delete_courier_without_id()
        self.check_response_message_of_delete_courier_without_id()
