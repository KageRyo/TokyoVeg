import pytest
from django.contrib.admin.sites import site
from ..models import Place, Photo, Tag, Tag_Management, Device, Device_Management

def test_admin_registration():
    assert site.is_registered(Place)
    assert site.is_registered(Photo)
    assert site.is_registered(Tag)
    assert site.is_registered(Tag_Management)
    assert site.is_registered(Device)
    assert site.is_registered(Device_Management)