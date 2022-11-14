from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Moto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    anio = models.IntegerField()


def __str__(self):
    return f'Marca: {self.marca} - Modelo: {self.modelo}'