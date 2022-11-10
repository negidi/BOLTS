from django.contrib import admin
from inventario import views
from django.urls import path

urlpatterns = [


    path('', views.index),
    path('crearHerramientas/', views.crearHerramientas),
    path('registrarHtas/', views.registrarHerramienta),
    path ('respuestaHtas/', views.respuestaHtas),
    path ('home/', views.home),
    path ('login/', views.login)

]