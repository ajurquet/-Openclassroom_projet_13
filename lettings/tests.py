import factory
from faker import Faker
from .models import Address, Letting
import pytest
from django.urls import reverse
from pytest_factoryboy import register

fake = Faker('en_US')


class AdressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address
    
    number = fake.random_int(min=1, max=9998)
    street = fake.street_name()
    city = fake.city()
    state = fake.city_suffix()
    zip_code = fake.random_int(min=1000, max=9998)
    country_iso_code = "USA"


class LettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Letting
    
    title = fake.company()
    address = factory.SubFactory(AdressFactory)


register(AdressFactory)
register(LettingFactory)


@pytest.fixture
def letting(db, letting_factory):
    
    letting = letting_factory.create()
    return letting


@pytest.mark.django_db
def test_letting_index_access(client):
    
    url = reverse("lettings_index")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_lettings_access(client, letting):
      
    url = reverse('letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    assert response.status_code == 200