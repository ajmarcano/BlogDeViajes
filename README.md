# Proyecto Blog de Viajes para clase de CoderHouse

## Verificar que tengas Python

Para comenzar primero tienen que asegurarse que tienen instalado, python.

En windows tiene que abrir una terminal cmd o powershell.

```PS
PS C:\> python --version
Python 3.X.X 
```

En Linux/Mac tiene que abrir una terminal bash

```bash
$ python --version
Python 3.X.X 
```

Si les aparece la versión todo OK pueden seguir. Caso contrario descarguen python desde este [link](https://www.python.org/downloads/).

## Instalar django

En una terminal cmd o powershell desde windows:

```PS
C:\> pip install django
```

Linux/Mac:

```bash
$ pip install django
```

Si no arrojo errores esto es suficiente para poder correr el projecto.


## Clonar el projecto con git

windows:

```PS
C:\> git clone https://github.com/martinezger/mi-primer-mvt.git
```

Linux/Mac:
```bash
$ git clone https://github.com/martinezger/mi-primer-mvt.git
```

## Correr el Servidor

Los siguientes comandos son análogos en Mac/Linux/Windows:

```bash
cd mi-primer-mvt
python manage.py migrate
```
La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web

```bash
python manage.py runserver
```
Listo ya tenes corriendo el ejemplo.

ahora Hace click en el siguiente link para ver el ejemplo corriendo: 

[http://localhost:8000/](http://localhost:8000/)

# Partes de la pagina:

## Pagina principal

Aqui tenemos la visualizacion de 2 modelos:

1. **Modelo Viaje()**, el cual nos enseña una cuadricula con distintos destinos agregados por usuarios de la pagina.
2. **Modelo Aeropuerto()**, que es una cuadricula la cual muestra una variedad de calificaciones a aeropuertos internacionales

Asimismo, tenemos un formulario de suscripcion a la pagina para recibir correos con actualizaciones

## Agregar Viajes y Agregar Aeropuertos

Formularios para agregar reseñas Viajes/Aeropuertos a la pagina principal

## Buscar Viajes/Aeropuertos

Formularios de busqueda para filtrar un viaje o aeropuerto en la pagina principal
