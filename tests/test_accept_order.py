import allure
from endpoints.accept_order import AcceptOrder


class TestAcceptOrder:
    @allure.title('Проверка принятия заказа')
    @allure.description('При успешном принятии заказа код ответа: 202, тело ответа: {"ok": True}')
    def test_accept_order(self, new_order_id, id_of_new_courier):
        accept_order = AcceptOrder()

        accept_order.accept_order(new_order_id, id_of_new_courier)

        accept_order.check_response_of_successful_accept_order()

    @allure.title('Проверка принятия заказа без id курьера')
    @allure.description('При  принятии заказа без id курьера код ответа: 400, сообщение в теле : "Недостаточно '
                        'данных для поиска')
    def test_accept_order_without_courier_id(self, new_order_id):
        accept_order = AcceptOrder()

        accept_order.accept_order(new_order_id)

        accept_order.check_response_status_code_of_accept_order_without_courier_or_order_id()

    @allure.title('Проверка принятия заказа c несуществующим id курьера')
    @allure.description('При  принятии заказа c несуществующим id курьера код ответа: 404, сообщение в теле : '
                        '"Курьера с таким id не существует"')
    def test_accept_order_with_not_existing_courier_id(self, new_order_id):
        accept_order = AcceptOrder()
        not_existing_courier_id = accept_order.generate_random_id()

        accept_order.accept_order(new_order_id, not_existing_courier_id)

        accept_order.check_response_of_accept_order_with_not_existing_courier_id()

    @allure.title('Проверка принятия заказа без номера заказа')
    @allure.description('При  принятии заказа без номера заказа код ответа: 400, сообщение в теле : "Недостаточно '
                        'данных для поиска')
    def test_accept_order_without_order_id(self, id_of_new_courier):
        accept_order = AcceptOrder()

        accept_order.accept_order(courier_id=id_of_new_courier)

        accept_order.check_response_status_code_of_accept_order_without_courier_or_order_id()

    @allure.title('Проверка принятия заказа c несуществующим id заказа')
    @allure.description('При  принятии заказа c несуществующим id курьера код ответа: 404, сообщение в теле : '
                        '"Заказа с таким id не существует"')
    def test_accept_order_with_not_existing_order_id(self, id_of_new_courier):
        accept_order = AcceptOrder()
        not_existing_order_id = accept_order.generate_random_id()

        accept_order.accept_order(not_existing_order_id, id_of_new_courier)

        accept_order.check_response_of_accept_order_with_not_existing_order_id()
