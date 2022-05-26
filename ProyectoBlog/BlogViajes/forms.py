from django import forms

class Entrada(forms.Form):
    destino = forms.CharField(label="Destino", max_length=100)
    imagen = forms.URLField(label="Imagen")
    reseña = forms.CharField(label="Reseña", max_length=100)
    autor = forms.Charfield(label="Autor", max_length=100)
 