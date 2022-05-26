from django.contrib import admin
from django.urls import path
from BlogViajes import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', views.index),
    path('agregar/', views.agregar, name="agregar"),
]