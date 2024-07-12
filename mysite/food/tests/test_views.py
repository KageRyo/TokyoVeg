import pytest
from django.urls import reverse
from django.test import Client
from ..models import Place, Photo, Tag, Device

# 首頁的測試
@pytest.mark.django_db
def test_index():
    client = Client()
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'food/index.html' in [template.name for template in response.templates]
    assert 'store_list' in response.context
    assert 'tags' in response.context
    assert 'devices' in response.context
    
# 子頁面的測試
@pytest.mark.django_db
def test_placeIntroduction():
    place = Place.objects.create(
        name = "Test Store",
        address = "Tokyo",
        pub_date = '2000-01-01 00:00:00',
        phone_number = '1234567890',
        website = 'https://example.com',
        introduction = 'This is a TEST STORE'   
    )
    client = Client()
    response = client.get(reverse('food_introduction', args=[place.id]))
    assert response.status_code == 200
    assert 'food/place_introduction.html' in [template.name for template in response.templates]
    assert 'store' in response.context
    assert 'photo_list' in response.context
    assert 'tags' in response.context
    assert 'devices' in response.context