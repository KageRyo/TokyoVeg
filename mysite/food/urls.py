from django.urls import path
from .views import index, place_introduction

urlpatterns = [
    path('', index),
    path('<int:place_id>/', place_introduction, name='food_introduction'),
]