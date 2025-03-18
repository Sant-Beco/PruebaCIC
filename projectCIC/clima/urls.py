from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crear/", views.crear_datos, name="crear_datos"),
    path("editar/<int:id>/", views.editar_datos, name="editar_datos"),
    path("eliminar/<int:id>/", views.eliminar_datos, name="eliminar_datos"),
    path("graficos/", views.graficos, name="graficos"),
]
