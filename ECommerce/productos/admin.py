from django.contrib import admin

from .models import Producto
# Register your models here.

#admin.site.register(Producto)
@admin.register(Producto)
class AdminProductos(admin.ModelAdmin):
    list_display=('id','nombre','categoria')
    list_filter=('categoria',)