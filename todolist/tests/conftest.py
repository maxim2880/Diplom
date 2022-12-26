import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
import factories

USER_MODEL = get_user_model()


@pytest.fixture
def auth_client():
    client = APIClient()
    client.force_authenticate(test_user)
    return client


@pytest.fixture
def test_user(db):
    user = USER_MODEL.objects.create(
        username='max',
        password='Ttest1234',
        email='max@mail.ru'
    )
    return user


@pytest.fixture
def category(board, test_user):
    return factories.GoalCategoryFactory.create(
        board=board,
        user=test_user,
    )


@pytest.fixture
def board():
    return factories.BoardFactory.create()


@pytest.fixture
def board_participant(test_user, board):
    participant = factories.BoardParticipantFactory.create(
        board=board,
        user=test_user,
    )
    return participant
