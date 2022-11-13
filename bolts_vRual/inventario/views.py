from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import activo
from .models import herramientas
from .models import maquinaria
from .models import permisos



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
    codigo_htas = request.POST['cod_herramienta']
    proveedor_htas = request.POST['proveedor']
    marca_htas = request.POST['marca']

    x = activo.objects.create(
        id_activo=id_htas, nombre_activo=nombre_htas, cantidad=cantidad_htas, precio=precio_htas)
    herramientas.objects.create(
        cod_herramienta=codigo_htas, proveedor=proveedor_htas, marca=marca_htas, activo=x)

    return render(request, 'respuestaHtas.html', {"mensaje": mensaje})


def crearMaquinaria(request):

    return render(request, 'crearMaquinaria.html')


def registrarMaquinaria(request):

    mensaje = "Se creo Ok"
    id_mqnas = request.POST['id_activo']
    nombre_mqnas = request.POST['nombre_activo']
    cantidad_mqnas = request.POST['cantidad']
    precio_mqnas = request.POST['precio']
    codigo_mqnas = request.POST['cod_maquina']
    diseno_mqnas = request.POST['disenomaq']
    estruc_mqnas = request.POST['estructuramaq']

    y = activo.objects.create(id_activo=id_mqnas, nombre_activo=nombre_mqnas,
                              cantidad=cantidad_mqnas, precio=precio_mqnas)
    maquinaria.objects.create(cod_maquinaria=codigo_mqnas,
                              diseño_maquinaria=diseno_mqnas, material_estructura=estruc_mqnas, activo=y)

    return render(request, 'respuestaHtas.html', {"mensaje": mensaje})


def actualizarmaq(request):
    return render(request, "actualizarmaquina.html")


def actualizarherr(request):
    return render(request, "actualizarherramientas.html")


def editarmaq(request):
    maq = None
    mensaje = ""
    try:
        maq = maquinaria.objects.get(activo=request.GET["idactivo"])
        act = activo.objects.get(id_activo=request.GET["idactivo"])
        return render(request, "actualizarmaquina.html", {"maqui": maq, "acti": act})
    except:
        maq = None

    if maq == None:
        id_activom = None
        try:
            id_activom = request.POST["id_activom"]
        except:
            id_activom = None

        if id_activom != None:
            maq = maquinaria.objects.get(activo=id_activom)
            act = activo.objects.get(id_activo=id_activom)

            nombre_a = request.POST["nombre_maquina"]
            cantidad_a = request.POST["cantidad"]
            precio_a = request.POST["precio"]
            disenomaq_a = request.POST["disenomaq"]
            estructuramaq_a = request.POST["estructuramaq"]
            act.nombre_activo = nombre_a
            act.cantidad = cantidad_a
            act.precio = precio_a
            maq.diseño_maquinaria = disenomaq_a
            maq.material_estructura = estructuramaq_a

            try:
                act.save()
                maq.save()
                mensaje = "Se ha actualizado"
            except:
                mensaje = "Ha ocurrido un error al actualizar"

            return render(request, "actualizarmaquina.html", {"mensaje": mensaje})

        else:
            mensaje = "No se ha encontrado la maquina"

            return render(request, "actualizarmaquina.html", {"mensaje": mensaje})
    else:
        mensaje = "No se encontró la maquina"

        return render(request, "actualizarmaquina.html", {"mensaje": mensaje})


def editarherr(request):
    herr = None
    mensaje = ""
    try:
        herr = herramientas.objects.get(activo=request.GET["idactivo"])
        act = activo.objects.get(id_activo=request.GET["idactivo"])
        return render(request, "actualizarherramientas.html", {"herra": herr, "acti": act})
    except:
        herr = None

    if herr == None:
        id_activom = None
        try:
            id_activom = request.POST["id_activom"]
        except:
            id_activom = None

        if id_activom != None:
            herr = herramientas.objects.get(activo=id_activom)
            act = activo.objects.get(id_activo=id_activom)

            nombre_a = request.POST["nombre_maquina"]
            cantidad_a = request.POST["cantidad"]
            precio_a = request.POST["precio"]
            proveedorherr_a = request.POST["proveedorherr"]
            marcaherr_a = request.POST["marcaherr"]
            act.nombre_activo = nombre_a
            act.cantidad = cantidad_a
            act.precio = precio_a
            herr.proveedor = proveedorherr_a
            herr.marca = marcaherr_a

            try:
                act.save()
                herr.save()
                mensaje = "Se ha actualizado"
            except:
                mensaje = "Ha ocurrido un error al actualizar"

            return render(request, "actualizarherramientas.html", {"mensaje": mensaje})

        else:
            mensaje = "No se ha encontrado la herramienta"

            return render(request, "actualizarherramientas.html", {"mensaje": mensaje})
    else:
        mensaje = "No se encontró la herramienta"

        return render(request, "actualizarherramientas.html", {"mensaje": mensaje})


def respuestaHtas(request):
    return render(request, "respuestaHtas.html")


def home(request):
    return HttpResponse("Inicio")

def login(request):
    return render (request,"login.html")


##def createRol():   
       ## permisos.objects.create(id_permisos=1,nombre_permiso='Laura')
        ##msj = 'se ha ingresado el permiso'
        
##createRol()
    
def sesion(request):
    per = None
    try:
        per = permisos.objects.get(id_permiso = int(request.POST["id_permiso"]))
        if(per.nombre_permiso == request.POST["contrasenna"]):
            request.session["sesion_activa"] = "Activa"
            return render(request,"home.html")
        else:
            return render(request,"login.html")
    except Exception as ex:
        return render(request,"login.html", {"mensaje":ex})
    
def homelogin(request):
    return render(request,"homelogin.html")