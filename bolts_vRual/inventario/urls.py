from django.contrib import admin
from inventario import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('inventario.urls')),
    
    path("accounts/", include("django.contrib.auth.urls"))
    
    ]


urlpatterns = [


    path('', views.index),
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
    path ('home/', views.home),
    path ('inicio/', views.home),
    path ('login/', views.login),
    path ('login/homelogin', views.homelogin),

]