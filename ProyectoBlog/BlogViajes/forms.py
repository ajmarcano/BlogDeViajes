from django import forms

class Entrada(forms.Form):
    destino = forms.CharField(label="Destino", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre del destino'}))
    imagen = forms.URLField(label="Imagen", widget=forms.TextInput(attrs={'placeholder': 'http://www.imagen.com'}))
    reseña = forms.CharField(label="Reseña", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Breve reseña de tu destino'}))
    autor = forms.CharField(label="Autor", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre y Apellido del autor'}))

class BusquedaEntradas(forms.Form):
    entrada_a_buscar = forms.CharField(label="Buscar")