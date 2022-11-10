from django.contrib import admin
from inventario import views
from django.urls import path

urlpatterns = [


    path('', views.index),
    path('crearHerramientas/', views.crearHerramientas),
    path('registrarHerramienta/', views.registrarHerramienta),
    path('crearMaquinaria/', views.crearMaquinaria),
    path('registrarMaquinaria/', views.registrarMaquinaria),
    path ('home/', views.home),
    path ('login/', views.login)

]