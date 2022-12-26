import pytest
from django.urls import reverse
from datetime import datetime
from rest_framework import status


@pytest.mark.django_db
def test_create(auth_client, category):
    url = reverse('create_goal')
    test_date = str(datetime.now().date())
    response = auth_client.post(
        path=url,
        data={
            'title': 'New Goal',
            'category': category.pk,
            'description': 'This is so wonderful goal',
            'due_date': test_date,
        }
    )

    assert response.status_code == status.HTTP_201_CREATED
