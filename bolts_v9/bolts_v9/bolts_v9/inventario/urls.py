from django.contrib import admin
from inventario import views
from django.urls import path

urlpatterns = [


    path('', views.home),
    path('crearHerramientas/', views.crearHerramientas),
    path('registrarHerramienta/', views.registrarHerramienta),
    path('crearMaquinaria/', views.crearMaquinaria),
    path('registrarMaquinaria/', views.registrarMaquinaria),
    path('actualizarmaq/', views.actualizarmaq),
    path('editarmaq/', views.editarmaq),
    path('editarmaq/editarmaq', views.editarmaq),
    path('editarherr/', views.editarherr),
    path('actualizarherr/', views.actualizarherr),
    path('editarherr/editarherr', views.editarherr),
    path('crearclientes/', views.crearclientes),
    path('registrarCliente/', views.registrarCliente),
    path('crearusuarios/', views.crearusuarios),
    path('registrarUsuario/', views.registrarUsuario),
    path('listarherramientas/', views.listarherramientas),
    path('listarmaquinaria/', views.listarmaquinaria),
    path('listarclientes/', views.listarclientes),
    path('filtroherr/', views.filtroherr),
    path('filtroclnte/', views.filtroclnte), 
    path ('home/', views.home),
    path ('login/', views.login)


]