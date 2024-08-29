import allure
from endpoints.create_order import CreateOrder
from endpoints.get_order_list import GetOrderList


class TestGetOrderList:
    @allure.title('Проверка получения списка заказов')
    @allure.description('При успешном получении списка заказов код ответа: 200, в теле ответа возвращается список '
                        'заказов')
    def test_get_order_list(self, payload_of_new_order):
        create_order = CreateOrder()
        create_order.create_order(payload_of_new_order)
        get_order_list = GetOrderList()

        get_order_list.get_order_list()

        get_order_list.check_response_getting_order_list()
