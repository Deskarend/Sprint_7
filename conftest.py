import random
import datetime
import pytest
from faker import Faker

from data import generate_random_string
from endpoints.create_courier import CreateCourier
from endpoints.create_order import CreateOrder
from endpoints.delete_courier import DeleteCourier
from endpoints.get_order_by_track import GetOrderByTrack
from endpoints.login_courier import LoginCourier

fake = Faker(locale='ru_RU')


@pytest.fixture
def payload_for_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": fake.first_name()
    }

    yield payload

    login_courier = LoginCourier()
    payload = {
        "login": login,
        "password": password
    }
    login_courier.login_courier(payload)

    if login_courier.response.status_code == 200:
        courier_id = login_courier.get_id_courier()

        delete_courier = DeleteCourier()
        delete_courier.delete_courier(courier_id)


@pytest.fixture
def login_and_password_of_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": fake.first_name()
    }

    create_courier = CreateCourier()
    create_courier.create_courier(payload)

    log_and_pass = {
        "login": login,
        "password": password
    }

    yield log_and_pass

    login_courier = LoginCourier()
    login_courier.login_courier(log_and_pass)
    courier_id = login_courier.get_id_courier()
    delete_courier = DeleteCourier()
    delete_courier.delete_courier(courier_id)


@pytest.fixture
def id_of_new_courier(login_and_password_of_new_courier):
    login_courier = LoginCourier()
    login_courier.login_courier(login_and_password_of_new_courier)

    return login_courier.get_id_courier()


@pytest.fixture
def payload_of_new_order():
    firstname = fake.first_name()
    lastname = fake.last_name()
    address = fake.address()
    metro_station = random.randint(1, 10)
    phone = fake.phone_number()
    rent_time = random.randint(1, 10)
    delivery_date = str((datetime.date.today() + datetime.timedelta(days=random.randint(1, 7))))
    comment = generate_random_string(10)

    return {
        'firstName': firstname,
        'lastName': lastname,
        'address': address,
        'metroStation': metro_station,
        'phone': phone,
        'rentTime': rent_time,
        'deliveryDate': delivery_date,
        'comment': comment,
        'color': []

    }


@pytest.fixture
def track_of_new_order(payload_of_new_order):
    create_order = CreateOrder()

    create_order.create_order(payload_of_new_order)

    return create_order.get_order_track()


@pytest.fixture
def new_order_id(track_of_new_order):
    get_order_by_track = GetOrderByTrack()

    get_order_by_track.get_order_by_track(track_of_new_order)

    return get_order_by_track.get_order_id()
