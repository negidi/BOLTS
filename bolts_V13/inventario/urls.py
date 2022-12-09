from django.contrib import admin
from inventario import views
from django.urls import path
from django.urls import path



urlpatterns = [

    path("", views.login_request), 
    path('home', views.home),
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
    path('actualizarcliente/', views.actualizarcliente),
    path('editarclte/', views.editarclte),
    path('editarclte/editarclte', views.editarclte),
    path('crearclientes/', views.crearclientes),
    path('registrarCliente/', views.registrarCliente),
    path('listarherramientas/', views.listarherramientas),
    path('listarmaquinaria/', views.listarmaquinaria),
    path('listarclientes/', views.listarclientes),
    path('listarusuario/', views.listarusuario),
    path('filtroherr/', views.filtroherr),
    path('filtroclnte/', views.filtroclnte),
    path('filtromaqu/', views.filtromaqu), 
    path ('home/', views.home),
    path("signup/signup", views.signup),
    path("auth/signup/", views.signup),
    path("logout/", views.logout_request),
    path("auth/login", views.login_request), 
    path("auth/login_request", views.login_request),
    path("/auth/logout/", views.logout_request),
    path('actualizarusuario/', views.actualizarusuario),
    path('editarus/', views.editarus),
    path('editarus/editarus', views.editarus),
    path("login", views.login_request), 

    
    
   
]