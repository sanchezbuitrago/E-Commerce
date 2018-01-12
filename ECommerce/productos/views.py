from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Producto
from .forms import ProductoForm

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

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    template = loader.get_template('detalle_producto.html')
    context = {
        'producto':producto,
    } 
    return HttpResponse(template.render(context,request))
     
def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            producto = form.save()
            producto.save()
            return HttpResponseRedirect('/productos/')
        else:
            print "Formulario no valido"
    else:
        form = ProductoForm()
    
    template = loader.get_template('producto_nuevo.html')
    context = {
        'form' : form
    }

    return HttpResponse(template.render(context,request))

