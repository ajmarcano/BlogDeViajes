from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request, "principal.html")

def agregar(request):
    return render(request, "agregar.html")

def buscar(request):
    return render(request, "buscar.html")
