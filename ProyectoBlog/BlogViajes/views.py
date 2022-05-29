from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from BlogViajes.models import Viaje
from BlogViajes.forms import Entrada

# Create your views here.

def principal(request):
    viajes = Viaje.objects.all()

    context = {'viajes': viajes}

    return render(request, "principal.html", context)

def agregar(request):

    if request.method == "POST":

        formulario = Entrada(request.POST)

        if formulario.is_valid():

            Destino = formulario.cleaned_data['destino']
            Imagen = formulario.cleaned_data['imagen']
            Reseña = formulario.cleaned_data['reseña']
            Autor = formulario.cleaned_data['autor']
            Viaje ( Destino=Destino, Imagen=Imagen, Reseña=Reseña, Autor=Autor ).save()

            return HttpResponseRedirect("/BlogViajes")

    elif request.method == "GET":
        formulario = Entrada()

    else:
        return HttpResponseBadRequest("Error. No reconozco ese comando")

    return render(request, "agregar.html", {"formulario":formulario})

def buscar(request):
    return render(request, "buscar.html")
    
    