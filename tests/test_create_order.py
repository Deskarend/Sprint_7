import allure
import pytest
from endpoints.create_order import CreateOrder


class TestCreateOrder:
    @allure.title('Проверка создания заказа с цветом')
    @allure.description('При создании заказа с цветом код ответа: 201, в теле ответа содержится track')
    @pytest.mark.parametrize('color', ['BLACK',
                                       'GREY',
                                       ['GREY', 'BLACK']])
    def test_create_order_with_color(self, payload_of_new_order, color):
        create_order = CreateOrder()
        create_order.add_color(payload_of_new_order, color)

        create_order.create_order(payload_of_new_order)

        create_order.check_response_successful_create_order()

    @allure.title('Проверка создания заказа без цвета')
    @allure.description('При создании заказа без цвета код ответа: 201, в теле ответа содержится track')
    def test_create_order_without_color(self, payload_of_new_order):
        create_order = CreateOrder()

        create_order.create_order(payload_of_new_order)

        create_order.check_response_successful_create_order()
