import json

import allure
import requests

from data import urls, helpers


class TestLoginUser:
    @allure.title("Успешний логин пользователя с корректными данными")
    @allure.description("Проверка успешной авторизации пользователя с корректными данными")
    def test_login_user_with_correct_data_success(self, register_new_user_return_user_data):
        response = helpers.login_user(register_new_user_return_user_data['email'],
                                      register_new_user_return_user_data['password'])
        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user']['email'] == str(register_new_user_return_user_data.get('email'))
        assert response.json()['user']['name'] == str(register_new_user_return_user_data.get('name'))

    @allure.title("Авторизация пользователя с некорректными данными")
    @allure.description("Проверка ошибки авторизации пользователя с некорректными данными")
    def test_login_user_with_incorrect_mail_and_password(self):
        random_email = f'{helpers.generate_random_string(10)}@mail.ru'
        random_password = helpers.generate_random_string(10)
        response = helpers.login_user(random_email, random_password)

        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == 'email or password are incorrect'
