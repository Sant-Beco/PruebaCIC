from django.urls import path
from .views import index, crear_datos, editar_datos, eliminar_datos

urlpatterns = [
    path('', index, name='index'),
    path('crear/', crear_datos, name='crear_datos'),
    path('editar/<int:id>/', editar_datos, name='editar_datos'),  # Nueva URL para editar
    path('eliminar/<int:id>/', eliminar_datos, name='eliminar_datos'),  # Nueva URL para eliminar
]   
