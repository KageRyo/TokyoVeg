import datetime
from typing import List, Optional
from ninja import NinjaAPI, Schema
from .models import Place, Photo, Tag, Tag_Management, Device, Device_Management

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
    photo: Optional[list[PhotoSchema]]
    website: str = "https://example.com"
    introduction: str = "店家資訊"
    pub_date: datetime.datetime
    tag: list[TagsSchema]
    devices: list[DevicesSchema]

@api.get("tags", response=List[TagsSchema])
def tags(request):
    tag = Tag.objects.all()
    return tag

@api.get("Devices", response=List[DevicesSchema])
def devices(request):
    device = Device.objects.all()
    return device