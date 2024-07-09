from django.contrib import admin
from .models import Place, Photo

admin.site.register(Place, admin.ModelAdmin)  # 商店資訊
admin.site.register(Photo, admin.ModelAdmin)  # 商店照片