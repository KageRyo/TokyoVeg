import datetime
from typing import List, Optional
from ninja import NinjaAPI, Schema
from .models import Place, Photo, Tag, Device

api = NinjaAPI()

class TagsSchema(Schema):
    name: str
    
class DevicesSchema(Schema):
    name: str
    
class PhotoSchema(Schema):
    name: str = "照片"
    path: str = '/'
    
class PlaceSchema(Schema):
    id: int = 1
    name: str = "店家"
    address: str = "地址"
    phone_number: str = "電話"
    photo: Optional[List[PhotoSchema]]
    website: str = "https://example.com"
    introduction: str = "店家資訊"
    pub_date: datetime.datetime
    tags: List[TagsSchema]
    devices: List[DevicesSchema]

@api.get("tags", response=List[TagsSchema])
def tags(request):
    tag = Tag.objects.all()
    return tag

@api.get("devices", response=List[DevicesSchema])
def devices(request):
    device = Device.objects.all()
    return device

@api.get("places", response=List[PlaceSchema])
def places(request, tags: str = None):
    if tags:
        places = Place.objects.prefetch_related('photo_set', 'tags').filter(tags__name=tags)
    else:
        places = Place.objects.prefetch_related('photo_set', 'tags').all()
    result = [PlaceSchema(
        **place.__dict__,
        tags=[TagsSchema(name=t.name) for t in place.tags.all()],
        photo=[PhotoSchema(name=photo.name, path=photo.file.url) for photo in place.photo_set.all()],
        devices=[DevicesSchema(name=d.name) for d in place.devices.all()]
    ) for place in places]
    return result