import pytest


@pytest.fixture()
@pytest.mark.django_db
def get_token(client, django_user_model):
    """get users and tokens"""

    username = 'maxim_'
    password = 'Maxim123!'
    is_staff = True

    second_username = 'Mmaxim'
    second_password = 'Mmaxim123!'

    curr_user = django_user_model.objects.create_user(username=username, password=password, is_staff=is_staff)
    second_user = django_user_model.objects.create_user(username=second_username, password=second_password,
                                                        is_staff=is_staff)

    response = client.post("/core/token_login", {"username": username, "password": password})
    second_response = client.post("/core/token_login", {"username": second_username, "password": second_password})

    return curr_user, response.data['token'], second_user, second_response.data['token']