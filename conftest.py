import allure
import pytest
import requests

from data import helpers, urls


@allure.step("Регистрация нового пользователя и удаление после теста. Возвращаемые значения - name, email, password")
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
    user_data['create_user_response'] = response
    yield user_data
    requests.delete(urls.API_URL_DELETE_USER, headers={'Authorization': user_token})
