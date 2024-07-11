from django.shortcuts import render
from .models import Place, Photo, Tag, Device

def index(request):
    tags = Tag.objects.all()
    devices = Device.objects.all()
    places = Place.objects.all()

    try:
        food_style = request.GET.get('food_style')
        if food_style:
            places = places.filter(tags__id=food_style)
    except Exception:
        pass

    try:
        payment_type = request.GET.get('payment_type')
        if payment_type:
            places = places.filter(devices__id=payment_type)
    except Exception:
        pass

    store_list = []
    for place in places:
        photo = Photo.objects.filter(place=place).first()  # 假設每個 Place 有一張主要照片
        store_list.append({
            'place': place,
            'photo': photo.file if photo else None  # 如果沒有找到照片，設為 None
        })

    return render(
        request,
        'food/index.html',
        {
            'store_list': store_list,
            'tags': tags,
            'devices': devices,
        }
    )

def place_introduction(request, place_id: int):
    place = Place.objects.get(id=place_id)
    photo_list = place.photo_set.all()
    return render(
        request,
        'food/place_introduction.html',
        {
            'store': place,
            'photo_list': photo_list,
            'name': place.name,
            'address': place.address,
            'website': place.website,
            'phone_number': place.phone_number,
            'introduction': place.introduction
        }
    )