from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import *


# Register your models here.

class Admin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_autozoom = "500"


admin.site.register(Location, Admin)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title']