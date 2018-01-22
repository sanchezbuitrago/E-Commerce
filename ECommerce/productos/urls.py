from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^productos/',views.obtenerproductos),
    url(r'^detalle_producto/(?P<pk>[0-9]+)/$',views.detalle_producto),
    url(r'^imagen/(?P<image>[^/]+)/$',views.getimagen),
    url(r'^nuevo_producto/',views.nuevo_producto),
]
