from django.contrib import admin
from .models  import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)

class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)


class OwnerContactAdmin(admin.ModelAdmin):
     list_display = ('name', 'building', 'contact')


class BuildingImageAdmin(admin.ModelAdmin):
    list_display = ('building', 'is_primary')
    list_filter = ('is_primary',)
    list_editable = ('is_primary',)

class BuildingDetailAdmin(admin.ModelAdmin):
    list_display = ('building', 'building_info_value')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(BuildingInfo)
admin.site.register(BuildingInfoValue)
admin.site.register(BuildingDetail, BuildingDetailAdmin)
admin.site.register(BuildingAddress)
admin.site.register(BuildingImage, BuildingImageAdmin)
admin.site.register(OwnerContact, OwnerContactAdmin)


