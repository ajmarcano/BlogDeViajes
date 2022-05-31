from reprlib import aRepr
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from BlogViajes.models import Viaje, Aeropuerto, Suscriptor
from BlogViajes.forms import Entrada, BusquedaEntradas, Aeropuertos, BusquedaAero, Suscriptores
from django.template import loader

# Create your views here.

def principal(request):
    viajes = Viaje.objects.all()
    aeropuertos = Aeropuerto.objects.all()
    template = loader.get_template('principal.html')
    formulario = Suscriptores()

    if request.method == "POST":
        
        formulario = Suscriptores(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            apellido = formulario.cleaned_data['apellido']
            email = formulario.cleaned_data['email']
            Suscriptor (nombre=nombre, apellido=apellido, email=email).save()

            return HttpResponseRedirect("/BlogViajes", {'formulario':formulario})
    
    context = {'viajes': viajes, 'aeropuertos': aeropuertos, 'formulario': formulario}

    return HttpResponse(template.render(context, request))

def agregar(request):

    if request.method == "POST":

        formulario = Entrada(request.POST)

        if formulario.is_valid():

            destino = formulario.cleaned_data['destino']
            imagen = formulario.cleaned_data['imagen']
            reseña = formulario.cleaned_data['reseña']
            autor = formulario.cleaned_data['autor']
            Viaje ( destino=destino, imagen=imagen, reseña=reseña, autor=autor ).save()

            return HttpResponseRedirect("/BlogViajes")

    elif request.method == "GET":
        formulario = Entrada()

    else:
        return HttpResponseBadRequest("Error. No reconozco ese comando")

    return render(request, "agregar.html", {"formulario":formulario})

def agregarAeropuertos(request):

    if request.method == "POST":

        formulario = Aeropuertos(request.POST)

        if formulario.is_valid():

            nombre = formulario.cleaned_data['nombre']
            ciudad = formulario.cleaned_data['ciudad']
            imagen = formulario.cleaned_data['imagen']
            calificacion = formulario.cleaned_data['calificacion']
            autor = formulario.cleaned_data['autor']
            Aeropuerto ( nombre=nombre, ciudad=ciudad,imagen=imagen, calificacion=calificacion, autor=autor ).save()

            return HttpResponseRedirect("/BlogViajes")

    elif request.method == "GET":
        formulario = Aeropuertos()

    else:
        return HttpResponseBadRequest("Error. No reconozco ese comando")

    return render(request, "agregarAero.html", {"formulario":formulario})

def buscar(request):
    
    if request.GET.get("destino") and request.method == "GET":

       form_busqueda = BusquedaEntradas(request.GET)

       if form_busqueda.is_valid():
           viajes = Viaje.objects.filter(destino__icontains=request.GET.get("destino"))
           return render(request, 'principal.html', {'viajes': viajes})

    elif request.method=="GET":
        form_busqueda = BusquedaEntradas()
        return render(request, 'buscar.html', {'form_busqueda': form_busqueda})

def buscarAero(request):
    
    if request.GET.get("nombre") and request.method == "GET":

       form_busqueda = BusquedaAero(request.GET)

       if form_busqueda.is_valid():
           aeropuertos = Aeropuerto.objects.filter(nombre__icontains=request.GET.get("nombre"))
           return render(request, 'principal.html', {'aeropuertos': aeropuertos})

    elif request.method=="GET":
        form_busqueda = BusquedaAero()
        return render(request, 'buscarAero.html', {'form_busqueda': form_busqueda})