# Sprint_7
## Проект автоматизации тестирования API учебного сервиса «Яндекс.Самокат»
1. Основа для написания автотестов — фреймворк pytest и библиотека requests.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v.
4. Команда для генерирования Allure-отчета  — pytest tests.py --alluredir=allure_results.
5. Команда для формирования отчёта в формате веб-страницы — allure serve allure_results

# Failed tests:
TestCreateCourier:

* test_create_two_identical_logins
* test_create_two_identical_couriers: 

Не совпадают тексты ошибки
ОР: "Этот логин уже используется", ФР: "Этот логин уже используется. Попробуйте другой."


TestDeleteCourier:

* test_delete_courier_with_not_existing_id

Не совпадает текст ошибки

ОР: "Курьера с таким id нет", ФР: "Курьера с таким id нет."
* test_delete_courier_without_id

Не совпадает код и текст ошибки

ОР: код 400 и текст "Курьера с таким id нет", ФР: код 404 "Not Found."

TestAcceptOrder:
* test_accept_order_without_order_id
Не совпадает код и текст ошибки

ОР: код 400 и текст "Недостаточно данных для поиска", ФР: код 404 "Not Found."


