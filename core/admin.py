from django.contrib import admin
from .models import State, City 


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'is_active')
    list_filter = ('state', 'is_active',)
    list_editable = ('is_active',)


admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)




