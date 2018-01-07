from django.conf.urls import url
from django.contrib import admin

from .views import obtenerproductos

urlpatterns = [
    url(r'^productos/', obtenerproductos),
]
