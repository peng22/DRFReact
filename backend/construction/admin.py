from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
from .models import *



admin.site.register(Construction,LeafletGeoAdmin)
admin.site.register(Engineer,LeafletGeoAdmin)
admin.site.register(Cement_Supply,LeafletGeoAdmin)
