from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Libro(models.Model):

    nombre= models.CharField(max_length=100)  #variable
    autor= models.CharField(max_length=20)
    anio= models.IntegerField(default=2000)
    dechaAdquisicion=models.DateField()

    def __str__(self):
        return self.nombre

