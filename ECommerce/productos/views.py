from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Producto

# Create your views here.

def obtenerproductos(request):
    productos = Producto.objects.order_by('nombre')
    template = loader.get_template('index.html')

    for pro in productos:
        print 'producto #'+str(pro.id)
        print pro.imagen

    context = {
        'productos':productos
    }

    return HttpResponse(template.render(context,request))
     