import allure
import requests

from data import helpers, urls


class TestUserData:
    @allure.title("Смена email'а пользователя ")
    @allure.description("Проверка успешной смены email'а пользователя")
    def test_change_user_email_success(self, register_new_user_return_user_data):
        new_user_email = f'{helpers.generate_random_string(10)}@mail.ru'
        user_name = str(register_new_user_return_user_data.get('name'))
        user_token = register_new_user_return_user_data.get('token')
        response = helpers.change_user_data(new_user_email, user_name, user_token)

        assert response.status_code == 200
        assert response.json()['user']['email'] == new_user_email
        assert response.json()['user']['name'] == user_name

    @allure.title("Смена параметра name пользователя ")
    @allure.description("Проверка успешной смены параметра name пользователя")
    def test_change_user_name_success(self, register_new_user_return_user_data):
        new_user_name = helpers.generate_random_string(10)
        user_email = register_new_user_return_user_data.get('email')
        user_token = register_new_user_return_user_data.get('token')
        response = helpers.change_user_data(user_email, new_user_name, user_token)

        assert response.status_code == 200
        assert response.json()['user']['email'] == user_email
        assert response.json()['user']['name'] == new_user_name

    @allure.title("Смена email'а пользователя при некорректном токене")
    @allure.description("Проверка невозможности смены email'а пользователя при некорректном токене")
    def test_change_user_email_failed(self, register_new_user_return_user_data):
        new_user_email = f'{helpers.generate_random_string(10)}@mail.ru'
        user_name = str(register_new_user_return_user_data.get('name'))
        payload = {
            "email": new_user_email,
            "name": user_name
        }

        response = requests.patch(urls.API_URL_CHANGE_USER_DATA, data=payload, headers={'Authorization': ""})

        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'

    @allure.title("Смена параметра name пользователя при некорректном токене")
    @allure.description("Проверка невозможности смены параметра name пользователя при некорректном токене")
    def test_change_user_email_failed(self, register_new_user_return_user_data):
        new_user_name = helpers.generate_random_string(10)
        user_email = str(register_new_user_return_user_data.get('email'))
        payload = {
            "email": user_email,
            "name": new_user_name
        }

        response = requests.patch(urls.API_URL_CHANGE_USER_DATA, data=payload, headers={'Authorization': ""})

        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'




