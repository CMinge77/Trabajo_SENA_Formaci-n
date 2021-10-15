
from django.contrib import admin

# Register your models here.
from personas.models import Persona, Domicilio

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'domicilio')
    search_fields = ['nombre', 'id']
    list_filter = ('nombre',)

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Domicilio)