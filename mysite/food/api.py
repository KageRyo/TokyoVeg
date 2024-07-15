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
    id: int
    name: str
    address: str
    phone_number: str
    photos: Optional[List[PhotoSchema]]
    website: str
    introduction: str
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

# GET：取得所有店家，支持根據不同參數進行篩選
@api.get("places", response=List[PlaceSchema])
def get_places(request, food_style: Optional[int] = None, payment_type: Optional[int] = None):
    # 初始化篩選字典
    filters = {}
    
    # 根據 food_style 參數篩選
    if food_style is not None:
        filters['tags__id'] = food_style
        
    # 根據 payment_type 參數篩選
    if payment_type is not None:
        filters['devices__id'] = payment_type

    # 根據篩選條件取得店家
    places = Place.objects.filter(**filters).prefetch_related('photo_set', 'tags', 'devices')
    
    # 格式化回傳結果
    result = [
        PlaceSchema(
            id=place.id,
            name=place.name,
            address=place.address,
            phone_number=place.phone_number,
            photos=[PhotoSchema(name=photo.name, path=photo.file.url) for photo in place.photo_set.all()],
            website=place.website,
            introduction=place.introduction,
            pub_date=place.pub_date,
            tags=[TagSchema(name=tag.name) for tag in place.tags.all()],
            devices=[DeviceSchema(name=device.name) for device in place.devices.all()]
        )
        for place in places
    ]
    
    return result

# GET：取得特定店家
@api.get("place", response=PlaceSchema)
def get_place(request, id: int):
    place = Place.objects.prefetch_related('photo_set', 'tags', 'devices').get(id=id)
    result = PlaceSchema(
        id=place.id,
        name=place.name,
        address=place.address,
        phone_number=place.phone_number,
        photos=[PhotoSchema(name=photo.name, path=photo.file.url) for photo in place.photo_set.all()],
        website=place.website,
        introduction=place.introduction,
        pub_date=place.pub_date,
        tags=[TagSchema(name=tag.name) for tag in place.tags.all()],
        devices=[DeviceSchema(name=device.name) for device in place.devices.all()]
    )
    return result
    
# POST：新增標籤資料
@api.post("tags")
def post_tag(request, pay_load: TagSchema):
    tag = Tag.objects.create(**pay_load.dict())
    return {"id": tag.id}