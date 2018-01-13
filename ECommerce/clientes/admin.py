from django.contrib import admin

from models import Cliente

# Register your models here.

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    list_display = ('nombre','celular','email','direccion',)
    list_filter = ('nombre',)