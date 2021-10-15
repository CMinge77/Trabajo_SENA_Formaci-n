from django.contrib import admin
from .models import Servicio, Categoria_servicios
# Register your models here.

class CategoriaServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Categoria_servicios, CategoriaServicioAdmin)