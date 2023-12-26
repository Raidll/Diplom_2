import json
import string
import random

import requests

from data import urls


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def login_user(email, password):
    payload = {
        "email": email,
        "password": password
    }
    return requests.post(urls.API_URL_LOGIN_USER, data=payload)


def change_user_data(email, name, token):
    payload = {
        "email": email,
        "name": name
    }
    return requests.patch(urls.API_URL_CHANGE_USER_DATA, data=payload, headers={'Authorization': token})


def create_new_order(ingredients: list, token):
    payload = {"ingredients": ingredients}
    return requests.post(urls.API_CREATE_NEW_ORDER, data=payload, headers={'Authorization': token})


def get_user_orders(token):
    return requests.get(urls.API_GET_USER_ORDERS, headers={'Authorization': token})
