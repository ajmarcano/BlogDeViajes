from django.contrib import admin
from BlogViajes.models import Viaje, Suscriptor, Aeropuerto

# Register your models here.

admin.site.register(Viaje)

admin.site.register(Aeropuerto)

admin.site.register(Suscriptor)