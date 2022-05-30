from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from BlogViajes.models import Viaje
from BlogViajes.forms import Entrada, BusquedaEntradas
from django.template import loader

# Create your views here.

def principal(request):
    viajes = Viaje.objects.all()
    template = loader.get_template('principal.html')
    
    context = {'viajes': viajes}

    return HttpResponse(template.render(context, request))

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
    
    if request.GET.get("entrada_a_buscar") and request.method == "GET":

       form_busqueda = BusquedaEntradas(request.GET)

       if form_busqueda.is_valid():
           viajes = Viaje.objects.filter(destino__icontains=request.GET.get("entrada_a_buscar"))
           return render(request, 'BlogViajes/principal.html', {'viajes': viajes, 'resultados_busqueda': True})

    elif request.method=="GET":
        form_busqueda = BusquedaEntradas()
        return render(request, 'buscar.html', {'form_busqueda': form_busqueda})
