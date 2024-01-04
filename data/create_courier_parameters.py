from data import helpers

email_for_parameters = f'{helpers.generate_random_string(10)}@mail.ru'
password_for_parameters = helpers.generate_random_string(10)
name_for_parameters = helpers.generate_random_string(10)

payloads_for_parameters_without_required_fields = [
    [{"email": "", "password": password_for_parameters, "name": name_for_parameters}],
    [{"email": email_for_parameters, "password": "", "name": name_for_parameters}],
    [{"email": email_for_parameters, "password": password_for_parameters, "name": ""}]
]
