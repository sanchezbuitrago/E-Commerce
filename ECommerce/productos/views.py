from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Producto

# Create your views here.

def obtenerproductos(request):
    productos = Producto.objects.order_by('nombre')
    template = loader.get_template('index.html')
    context = {
        'productos':productos
    }

    return HttpResponse(template.render(context,request))
     