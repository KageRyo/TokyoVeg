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