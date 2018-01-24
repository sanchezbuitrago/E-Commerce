from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView

import sys

from .models import Producto
from .forms import ProductoForm

# Create your views here.
class ListaProductos(ListView):
    model = Producto

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListView,self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['host'] = self.request.get_host()
        return context

class DetalleProducto(DetailView):
    model = Producto

class NuevoProducto(CreateView):
    model = Producto
    fields = ('__all__')