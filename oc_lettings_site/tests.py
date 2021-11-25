import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test', 'test@test.com', 'test')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_index_access(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome to Holiday Homes" in response.content