from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Moto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    edad = models.IntegerField()