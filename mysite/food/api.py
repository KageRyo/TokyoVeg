import datetime
from typing import List, Optional
from ninja import NinjaAPI, Schema
from .models import Place, Photo, Tag, Device

api = NinjaAPI()

# 定義標籤的Schema
class TagSchema(Schema):
    name: str
    
# 定義設備的Schema
class DeviceSchema(Schema):
    name: str
    
# 定義照片的Schema
class PhotoSchema(Schema):
    name: str = "照片"
    path: str = '/'

# 定義店家的Schema
class PlaceSchema(Schema):
    id: int = 1
    name: str = "店家"
    address: str = "地址"
    phone_number: str = "電話"
    photos: Optional[List[PhotoSchema]]
    website: str = "https://example.com"
    introduction: str = "店家資訊"
    pub_date: datetime.datetime
    tags: List[TagSchema]
    devices: List[DeviceSchema]

# GET：取得所有標籤
@api.get("tags", response=List[TagSchema])
def get_tags(request):
    tags = Tag.objects.all()
    return tags

# GET：取得所有設備
@api.get("devices", response=List[DeviceSchema])
def get_devices(request):
    devices = Device.objects.all()
    return devices

# GET：取得所有店家
@api.get("places", response=List[PlaceSchema])
def get_places(request, tag_name: str = None):
    # 以標籤篩選取得店家
    if tag_name:
        places = Place.objects.prefetch_related('photo_set', 'tags').filter(tags__name=tag_name)
    else:
        places = Place.objects.prefetch_related('photo_set', 'tags').all()
        
    result = [
        PlaceSchema(
            **place.__dict__,   # 將 place 的所有屬性以關鍵字參數方式傳遞給 PlaceSchema
            tags=[TagSchema(name=tag.name) for tag in place.tags.all()],    # 與篩選項目符合的標籤
            photos=[PhotoSchema(name=photo.name, path=photo.file.url) for photo in place.photo_set.all()],  # 對應的照片
            devices=[DeviceSchema(name=device.name) for device in place.devices.all()]  # 對應的設備標籤
        )
        for place in places     # 列表生成式
    ]
    return result

# GET：取得特定店家
@api.get("place", response=PlaceSchema)
def get_place(request, id, int = 1):
    place = Place.objects.prefetch_related('photo_set', 'tags').get(id=id)
    result = PlaceSchema(
        **place.__dict__,
        tags=[TagSchema(name=tag.name) for tag in place.tags.all()],    # 與篩選項目符合的標籤
        photos=[PhotoSchema(name=photo.name, path=photo.file.url) for photo in place.photo_set.all()],  # 對應的照片
        devices=[DeviceSchema(name=device.name) for device in place.devices.all()]  # 對應的設備標籤
    )
    return result
    