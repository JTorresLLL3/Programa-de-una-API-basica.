"""
Configuración de URLs para la aplicación de gestión de usuarios:
- Define las rutas para las operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
- Cada ruta está asociada a una vista específica y tiene un nombre único para referencia
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('registro/', views.registro, name='registro'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path("modificar/<int:usuario_id>/", views.modificar_usuario, name="modificar"),
    path("eliminar/<int:usuario_id>/", views.eliminar_usuario, name="eliminar"),
]

