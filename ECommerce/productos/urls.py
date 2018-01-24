from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^productos/',views.ListaProductos.as_view(),name="listaproductos"),
    url(r'^detalle_producto/(?P<pk>[0-9]+)/$',views.DetalleProducto.as_view(),name="detalleproducto"),
    url(r'^nuevo_producto/',views.NuevoProducto.as_view(),name="nuevoproducto"),
]
