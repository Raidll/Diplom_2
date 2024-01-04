import allure

from data import helpers


class TestGetUserOrders:
    @allure.title("Успешное получение списка заказов")
    @allure.description("Проверка успешного получения списка заказов пользователя")
    def test_get_user_orders_success(self, register_new_user_return_user_data):
        user_token = register_new_user_return_user_data.get('token')
        ingredient_list = ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6c"]

        helpers.create_new_order(ingredient_list, user_token)
        get_orders_response = helpers.get_user_orders(user_token)

        assert get_orders_response.status_code == 200
        assert get_orders_response.json()['orders'][0]['ingredients'] == ingredient_list

    @allure.title("Ошибка получения списка заказов, если не передан токен")
    @allure.description("Проверка невозможности просмотря списка заказов при отсутствии токена в запросе")
    def test_get_user_orders_success(self, register_new_user_return_user_data):
        user_token = ""
        get_orders_response = helpers.get_user_orders(user_token)

        assert get_orders_response.status_code == 401
        assert get_orders_response.json()['message'] == "You should be authorised"
