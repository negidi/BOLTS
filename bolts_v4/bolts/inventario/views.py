from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from inventario.activo import Activo



# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')


def creacionActivo(request):

    return render(request, 'creacionActivo.html')


def respuesta(request):

    idActivo = request.POST["txt_id"]
    nombre = request.POST["txt_nombre"]
    cantidad = request.POST["txt_cantidad"]
    precio = request.POST["txt_precio"]
    tipo_activo = request.POST["txt_tipo_activo"]
    responsable = request.POST["txt_responsable"]
    

    Activos = (Activo(idActivo,nombre,cantidad,precio,tipo_activo,responsable))
    return render(request, 'respuesta.html', {"Activos":Activos})

def home(request):
    return render(request, 'home.html')




