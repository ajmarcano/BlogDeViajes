from django import forms

class Entrada(forms.Form):
    destino = forms.CharField(label="Destino", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre del destino'}))
    imagen = forms.URLField(label="Imagen", widget=forms.TextInput(attrs={'placeholder': 'http://www.imagen.com'}))
    reseña = forms.CharField(label="Reseña", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Breve reseña de tu destino'}))
    autor = forms.CharField(label="Autor", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre y Apellido del autor'}))

class BusquedaEntradas(forms.Form):
    destino = forms.CharField(label="Ingresa el nombre del destino a buscar:")

class BusquedaAero(forms.Form):
    nombre = forms.CharField(label="Ingresa el nombre del aeropuerto a buscar:")

class Aeropuertos(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre del aeropuerto'}))
    ciudad = forms.CharField(label="Ciudad", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ciudad donde se encuentra'}))
    imagen = forms.URLField(label="Imagen", widget=forms.TextInput(attrs={'placeholder': 'http://www.imagen.com'}))
    calificacion = forms.CharField(label="Calificación", max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Calificación del 1 al 5'}))
    autor = forms.CharField(label="Autor", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre y Apellido del autor'}))

class Suscriptores(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellido = forms.CharField(label="Apellido", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    email = forms.EmailField(label="Email", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'usuario@correo.com'}))