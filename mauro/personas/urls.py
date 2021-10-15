"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

from .views import detallepersona, nuevaPersona, editPersona, eliminarPersona
from webapp.views import bienvenido, conection_web
# from django.contrib.auth.view import login
# from Django.personas_django.sap.personas.views import index, new
# from personas_django.sap.personas import views

urlpatterns = [
    path('detalle_persona/<int:id>', detallepersona, name='detalle_persona'),
    #estamos creando un nuevo objeto dentro de personas
    path('nueva_persona/', nuevaPersona, name='mecanico'),
    path('edit_persona/<int:id>', editPersona, name='editar'),
    path('eliminar_persona/<int:id>', eliminarPersona, name='eliminar'),
    path('Inicio/', bienvenido, name='Inicio'),
    path('', conection_web),

]

# detallar contactos django y bases de datos en django

admin.site.site_header = "Administracion del Sistema"
admin.site.index_title = "KeepQuerry (ERS)"
admin.site.site_title = "Administracion KeepQuerry (ERS)"