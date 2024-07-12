import pytest
from ..models import Place, Photo, Tag, Device

# 對新增商店功能的測試
@pytest.mark.django_db
def test_createPlace():
    place = Place.objects.create(
        name = "Test Store",
        address = "Tokyo",
        pub_date = '2000-01-01 00:00:00',
        phone_number = '1234567890',
        website = 'https://example.com',
        introduction = 'This is a TEST STORE'   
    )
    assert place.name == 'Test Store'
    assert place.address == 'Tokyo'
    assert place.pub_date == '2000-01-01 00:00:00'
    assert place.phone_number == '1234567890'
    assert place.website == 'https://example.com'
    assert place.introduction == 'This is a TEST STORE'
    
# 對新增照片的測試
@pytest.mark.django_db
def test_uploadPhoto():
    place = Place.objects.create(
        name = "Test Store",
        address = "Tokyo",
        pub_date = '2000-01-01 00:00:00',
        introduction = 'This is a TEST STORE'   
    )
    photo = Photo.objects.create(
        name='Test Photo', 
        place=place, 
        file='./tests-images/test.jpg'
    )
    assert photo.name == 'Test Photo'
    assert photo.place == place
    
# 對標籤的測試
@pytest.mark.django_db
def test_tag():
    tag = Tag.objects.create(name = "全素")
    assert str(tag) == "全素"

# 對設備的測試
@pytest.mark.django_db
def test_device():
    device = Device.objects.create(name = "信用卡")
    assert str(device) == "信用卡"