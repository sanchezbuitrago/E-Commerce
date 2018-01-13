from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    celular = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre