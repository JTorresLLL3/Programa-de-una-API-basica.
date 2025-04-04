"""
URL configuration for example project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
Esta sección del código define las rutas principales del proyecto.
- Conecta URLs con vistas específicas de las apps 'polls' y 'myexample'.
- Incluye rutas para ver encuestas, registrar, buscar, modificar y eliminar usuarios.
- También habilita la interfaz de administración de Django.
"""

from django.contrib import admin
from django.urls import include, path
from polls import views as polls_views
from myexample import views as myexample_views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
    path('', polls_views.index),
    path('registro/', polls_views.registro, name='registro'),
    path('busqueda/', polls_views.busqueda, name='busqueda'),
    path('modificar/<int:id>/', myexample_views.modificar_usuario, name='modificar'),
    path('eliminar/<int:id>/', myexample_views.eliminar_usuario, name='eliminar'),
    path("", include("polls.urls")),
]


