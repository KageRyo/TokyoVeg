from django.shortcuts import render
from .models import Place, Photo

def index(request):
    photo = Photo.objects.first()
    place = Place.objects.all()
    return render(
        request,
        'food/index.html',
        {
            'store_list': place, 
            'photo': photo.file
        }
    )
    
def place_introduction(request, place_id: int):
    place = Place.objects.get(id=place_id)
    photo = Photo.objects.get(id=place_id)
    name = place.name
    address = place.address
    website = place.website
    phone_number = place.phone_number
    introduction = place.introduction
    return render(
        request,
        'food/place_introduction.html',
        {
            'store': place,
            'photo': photo.file,
            'name': name,
            'address': address,
            'website': website,
            'phone_number': phone_number,
            'introduction': introduction
        }
    )