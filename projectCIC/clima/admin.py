from django.contrib import admin
from .models import Datos

@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    list_display = ("ciudad", "temperatura", "humedad")
    search_fields = ("ciudad",)
    list_filter = ("ciudad",)
