import allure
import pytest
import requests

from data import helpers, urls


@allure.title("Регистрация нового пользователя и удаление после теста")
@allure.description("Регистрация пользователя, возврат response и удаление пользователя после теста")
@pytest.fixture
def register_new_user():
    email = f'{helpers.generate_random_string(10)}@mail.ru'
    password = helpers.generate_random_string(10)
    name = helpers.generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(urls.API_URL_CREATE_NEW_USER, data=payload)
    yield response
    user_token = response.json()['accessToken']
    requests.delete(urls.API_URL_DELETE_USER, headers={'Authorization': user_token})

@allure.title("Регистрация нового пользователя и удаление после теста. Возвращаемые значения - name, email, password")
@allure.description("Регистрация пользователя, возврат response и удаление пользователя после теста. Возвращаемые значения - name, email, password")
@pytest.fixture
def register_new_user_return_user_data():
    user_data = {}
    email = f'{helpers.generate_random_string(10)}@mail.ru'
    password = helpers.generate_random_string(10)
    name = helpers.generate_random_string(10)
    user_data['email'] = email
    user_data['password'] = password
    user_data['name'] = name

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(urls.API_URL_CREATE_NEW_USER, data=payload)
    user_token = response.json()['accessToken']
    user_data['token'] = user_token
    yield user_data
    requests.delete(urls.API_URL_DELETE_USER, headers={'Authorization': user_token})

