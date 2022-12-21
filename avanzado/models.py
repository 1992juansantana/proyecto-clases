from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Moto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    anio = models.IntegerField()
    portada = models.ImageField(upload_to='motos',null=True, blank=True)
    tipo = RichTextField(blank=True, null=True)
    vendedor = models.TextField(max_length = 20)


def __str__(self):
    return f'Marca: {self.marca} - Modelo: {self.modelo}'