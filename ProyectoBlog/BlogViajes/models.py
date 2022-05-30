from curses.textpad import Textbox
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, EmailField, URLField

# Create your models here.

class Viaje(models.Model):
    destino = models.CharField(max_length=20)
    imagen = models.URLField()
    reseña = models.TextField(max_length=400)
    autor = models.CharField(max_length=20)

    def __str__(self):
        return self.Destino

class Suscriptor(models.Model):
    Nombre = models.CharField(max_length=10)
    Apellido = models.CharField(max_length=10)
    Email = models.EmailField()




