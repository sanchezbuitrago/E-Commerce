from __future__ import unicode_literals
from django.conf import os

from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(blank=True)#, default='./default.jpg'

    def __str__(self):
        return self.nombre

    def save(self):
        if not self.imagen:
            print "Se tiene que agregar una imagen"
            self.imagen='./default.jpg'
        super(Producto,self).save()