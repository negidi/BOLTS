from django.contrib import admin
from inventario import views
from django.urls import path

urlpatterns = [


    path('', views.index),
    path('creacionActivo/', views.creacionActivo),
    path ('respuesta/', views.respuesta),
    path ('home/', views.home),
    path ('login/', views.login)

]