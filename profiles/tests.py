import factory
from faker import Faker
from .models import Profile
from django.contrib.auth.models import User
import pytest
from django.urls import reverse
from pytest_factoryboy import register

fake = Faker('en_US')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    password = fake.random_int(min=1000, max=99999)
    first_name = fake.first_name()
    last_name = fake.last_name()
    


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
    
    user = factory.SubFactory(UserFactory)
    favorite_city = fake.city()
    
register(UserFactory)
register(ProfileFactory)


@pytest.fixture
def profile(profile_factory):
    profile = profile_factory.create()
    return profile


@pytest.mark.django_db
def test_profile_list_access(client):
    url = reverse('profiles_index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_details_access(client, profile):

    url = reverse('profile', kwargs={'username': profile.user.username})
    response = client.get(url)
    assert response.status_code == 200