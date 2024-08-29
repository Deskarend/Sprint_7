import allure
from endpoints.get_order_by_track import GetOrderByTrack


class TestGetOrderByTrack:
    @allure.title('Проверка получения заказа по его трекинговому номеру')
    @allure.description('При успешном получении заказа по его трекиноговому номеру код ответа: 200, в теле ответа '
                        'возвращается объект с заказом ')
    def test_get_order_by_track(self, track_of_new_order):
        get_order_by_track = GetOrderByTrack()

        get_order_by_track.get_order_by_track(track_of_new_order)

        get_order_by_track.check_response_successful_getting_order_by_track()

    @allure.title('Проверка получения заказа по его трекинговому номеру без номера')
    @allure.description('При получении заказа по его трекиноговому номеру без номера код ответа: 400, в теле ответа '
                        '"Недостаточно данных для поиска"')
    def test_get_order_by_track_without_track(self):
        get_order_by_track = GetOrderByTrack()

        get_order_by_track.get_order_by_track()

        get_order_by_track.check_response_getting_order_by_track_without_track()

    @allure.title('Проверка получения заказа по его трекинговому номеру с несуществующим номером')
    @allure.description('При получении заказа по его трекиноговому номеру несуществующим номером код ответа: 404, '
                        'в теле ответа "Заказ не найден"')
    def test_get_order_by_track_with_not_existing_track(self):
        get_order_by_track = GetOrderByTrack()
        not_existing_track = get_order_by_track.generate_random_id()

        get_order_by_track.get_order_by_track(not_existing_track)

        get_order_by_track.check_response_getting_order_by_track_with_not_existing_track()
