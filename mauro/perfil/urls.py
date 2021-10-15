# from django.contrib import admin
from django.urls import path

from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [

    path('new/', new, name='new'),
    path('usuario', feed, name='usuario'),
    path('register', register, name='register'),
    path('', perfil, name='perfil'),
    path('perfil/<str:username>/', perfil, name='perfil'),
    path('login', LoginView.as_view(template_name='perfil/register.html'), name='login'),
    path('Salir', LogoutView.as_view(template_name='perfil/logau.html'), name='salir'),
    path('post', post, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
