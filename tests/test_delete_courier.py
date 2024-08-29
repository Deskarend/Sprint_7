import allure
from endpoints.delete_courier import DeleteCourier


class TestDeleteCourier:
    @allure.title('Проверка удаления курьера')
    @allure.description('При успешном удалении курьера код ответа: 200, тело ответа: {"ok": True}')
    def test_delete_courier(self, id_of_new_courier):
        delete_courier = DeleteCourier()

        delete_courier.delete_courier(id_of_new_courier)

        delete_courier.check_response_of_successful_delete()

    @allure.title('Проверка удаления несуществующего курьера')
    @allure.description('При удалении несуществующего курьера код ответа: 400, сообщение в теле : "Курьера с таким '
                        'id нет"')
    def test_delete_courier_with_not_existing_id(self):
        delete_courier = DeleteCourier()
        courier_id = DeleteCourier.generate_random_id()

        delete_courier.delete_courier(courier_id)

        delete_courier.check_response_of_delete_courier_with_not_existing_id()

    @allure.title('Проверка удаления курьера без id')
    @allure.description('При удалении курьера без id код ответа: 400, сообщение в теле : "Недостаточно данных для '
                        'удаления курьера')
    def test_delete_courier_without_id(self):
        delete_courier = DeleteCourier()

        delete_courier.delete_courier()

        delete_courier.check_response_of_delete_courier_without_id()
