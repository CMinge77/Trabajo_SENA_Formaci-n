from django.contrib import admin
from app.models import Servicio
# Register your models here.

# class PersonaAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'apellido', 'email', 'domicilio')
#     search_fields = ['nombre', 'id']
#     list_filter = ('nombre',)

admin.site.register(Servicio)