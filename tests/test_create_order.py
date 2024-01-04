import allure
import requests

from data import helpers, urls


class TestCreateOrder:
    @allure.title("Создание заказа")
    @allure.description("Проверка успешного создания заказа")
    def test_create_order_success(self, register_new_user_return_user_data):
        user_token = register_new_user_return_user_data.get('token')
        ingredient_list = ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6c"]

        create_response = helpers.create_new_order(ingredient_list, user_token)

        assert create_response.status_code == 200
        assert create_response.json()['success'] == True

    @allure.title("Создании заказа без авторизации")
    @allure.description("Проверка возможности создать заказ, если не передан токен")
    def test_create_order_success(self):
        ingredients = ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6c"]
        payload = {"ingredients": ingredients}

        create_response = requests.post(urls.API_CREATE_NEW_ORDER, data=payload, headers={'Authorization': ""})

        assert create_response.status_code == 200
        assert create_response.json()['success'] == True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка ошибки при создании заказа без ингредиентов")
    def test_create_order_success(self, register_new_user_return_user_data):
        user_token = register_new_user_return_user_data.get('token')
        ingredient_list = []

        create_response = helpers.create_new_order(ingredient_list, user_token)

        assert create_response.status_code == 400
        assert create_response.json()['message'] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешом ингредиента")
    @allure.description("Проверка ошибки при создании заказа, если передан неверный хеш ингредиента")
    def test_create_order_success(self, register_new_user_return_user_data):
        user_token = register_new_user_return_user_data.get('token')
        ingredient_list = ["001bdaaa75", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6c"]

        create_response = helpers.create_new_order(ingredient_list, user_token)

        assert create_response.status_code == 500


