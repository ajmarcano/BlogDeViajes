from django.shortcuts import render
from BlogViajes.forms import Entrada

# Create your views here.

def principal(request):
    return render(request, "principal.html")

def agregar(request):

    if request.method == "POST":

        formulario = Entrada(request.POST)

        print(formulario)

        if formulario.is_valid:

            informacion = formulario.cleaned_data

            entrada = Entrada ( destino=informacion["destino"], imagen=informacion["imagen"], reseña=informacion["reseña"], autor=informacion["autor"] )

            entrada.save()

            return render(request, r"C:\Users\Leisa\Downloads\ProyectoFinal-20220526T004057Z-001\ProyectoFinal\ProyectoBlog\BlogViajes\templates\principal.html")

    else:
        formulario = Entrada()

    return render(request, r"C:\Users\Leisa\Downloads\ProyectoFinal-20220526T004057Z-001\ProyectoFinal\ProyectoBlog\BlogViajes\templates\agregar.html", {"formulario":formulario})

def buscar(request):
    return render(request, "buscar.html")
    
    