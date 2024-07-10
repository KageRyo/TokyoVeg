from django.shortcuts import render
from .models import Place, Photo

def index(request):
    places = Place.objects.all()
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
            'store_list': store_list
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