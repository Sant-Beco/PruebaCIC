from django.urls import path
from .views import index, crear_datos

urlpatterns = [
    path('', index, name='index'),
    path('crear/', crear_datos, name='crear_datos'),
]   
