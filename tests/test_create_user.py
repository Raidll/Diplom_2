import json

import allure
import pytest
import requests

from data import helpers, urls, create_courier_parameters


class TestCreateUse:
    @allure.title("Регистрация пользователя с корректными данными")
    @allure.description("Проверка успешной регистрации пользователя с корректными данными")
    def test_create_user_with_correct_data_success(self, register_new_user_return_user_data):
        assert register_new_user_return_user_data['create_user_response'].status_code == 200
        assert register_new_user_return_user_data['create_user_response'].json()['success'] == True

    @allure.title("Регистрация пользователя с не уникальными данными")
    @allure.description(
        "Проверка недопустимости регистрации пользователя с данными, которые уже использовались при регистрации ранее")
    def test_create_not_unique_user_failed(self, register_new_user_return_user_data):
        response = register_new_user_return_user_data['create_user_response']
        email = response.json()['user']['email']
        password = helpers.generate_random_string(10)
        name = response.json()['user']['name']

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(urls.API_URL_CREATE_NEW_USER, data=payload)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title("Регистрация пользователя с не уникальным email")
    @allure.description(
        "Проверка недопустимости регистрации пользователя с email, который уже использовался при регистрации ранее")
    def test_create_user_with_not_unique_email(self, register_new_user_return_user_data):
        email = register_new_user_return_user_data['email']
        password = helpers.generate_random_string(10)
        name = helpers.generate_random_string(10)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(urls.API_URL_CREATE_NEW_USER, data=payload)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title("Регистрация пользователя с не уникальным именем")
    @allure.description(
        "Проверка недопустимости регистрации пользователя с именем, которое уже использовалось при регистрации ранее")
    def test_create_user_with_not_unique_email(self, register_new_user_return_user_data):
        email = f'{helpers.generate_random_string(10)}@mail.ru'
        password = helpers.generate_random_string(10)
        name = register_new_user_return_user_data['name']

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(urls.API_URL_CREATE_NEW_USER, data=payload)

        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title("Регистрация пользователя без одного из обязательных полей")
    @allure.description("Проверка недопустимости регистрации пользователя без указания одного из обязательных полей")
    @pytest.mark.parametrize('payload', create_courier_parameters.payloads_for_parameters_without_required_fields)
    def test_create_user_without_required_field_failed(self, payload):
        response = requests.post(urls.API_URL_CREATE_NEW_USER, data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
