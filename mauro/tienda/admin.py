from django.contrib import admin

# Register your models here.

from .models import CategoriaProd, Producto



class CategoriaProdAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class ProductoAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(CategoriaProd, CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)