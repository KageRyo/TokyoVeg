from django.contrib import admin
from .models import Place, Photo, Tag, Tag_Management, Device, Device_Management

class TagInlineAdmin(admin.StackedInline):
    model = Place.tags.through
    
class DeviceInlineAdmin(admin.StackedInline):
    model = Place.devices.through

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'website', 'pub_date')
    list_filter = ('pub_date', 'tags')
    search_fields = ('name', 'address', 'website')
    ordering = ('-id',)
    readonly_fields = ('pub_date',)
    inlines = [TagInlineAdmin, DeviceInlineAdmin]

admin.site.register(Place, PlaceAdmin)                      # 商店資訊
admin.site.register(Photo, admin.ModelAdmin)                # 商店照片
admin.site.register(Tag, admin.ModelAdmin)                  # 標籤
admin.site.register(Tag_Management, admin.ModelAdmin)       # 標籤與店家關聯
admin.site.register(Device, admin.ModelAdmin)               # 設備（付款方式）
admin.site.register(Device_Management, admin.ModelAdmin)    # 設備與店家關聯