from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import activo
from .models import herramientas



# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
def creacionActivo(request):

    return render(request, 'creacionActivo.html')

def crearHerramientas(request):

    return render(request, 'crearHerramientas.html')

def registrarHerramienta(request):
    mensaje = "Se creo Ok"
    id_htas = request.POST['id_activo']
    nombre_htas = request.POST['nombre_activo']
    cantidad_htas = request.POST['cantidad']
    precio_htas = request.POST['precio']
    codigo_htas = request.POST ['cod_herramienta']
    proveedor_htas = request.POST['proveedor']
    marca_htas = request.POST ['marca']

    
    herramientas.objects.create(id_activo = id_htas , nombre_activo = nombre_htas , cantidad = cantidad_htas ,
    precio = precio_htas ,  cod_herramienta = codigo_htas, 
    proveedor = proveedor_htas, marca = marca_htas )

    return render(request, 'respuestaHtas.html',{"mensaje": mensaje})


def respuestaHtas(request):
    return render(request, "respuestaHtas.html")


  






