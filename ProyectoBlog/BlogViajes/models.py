from re import M
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
        return self.destino

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre

class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    imagen = models.URLField()
    calificacion = models.CharField(max_length=2)
    autor = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre




