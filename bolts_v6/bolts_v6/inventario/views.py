from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import activo
from .models import herramientas
from .models import maquinaria
from .models import clientes
from .models import personas
from .models import roles
from .models import permisos
from .models import roles_permisos



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
    id_herramientas = request.POST['id_activo']
    nombre_herramientas = request.POST['nombre_activo']
    cantidad_herramientas = request.POST['cantidad']
    precio_herramientas = request.POST['precio']
    codigo_herramientas = request.POST ['cod_herramienta']
    proveedor_herramientas = request.POST['proveedor']
    marca_herramientas = request.POST ['marca']


    x = activo.objects.create(id_activo = id_herramientas , nombre_activo = nombre_herramientas , cantidad = cantidad_herramientas , precio = precio_herramientas)
    herramientas.objects.create(cod_herramienta = codigo_herramientas,proveedor = proveedor_herramientas, marca = marca_herramientas, activo = x)

    return render(request, 'respuestaHtas.html',{"mensaje": mensaje})

def crearMaquinaria(request):

    return render(request, 'crearMaquinaria.html')

def registrarMaquinaria(request):

    mensaje = "Se creo Ok"
    id_mqnas = request.POST['id_activo']
    nombre_mqnas = request.POST['nombre_activo']
    cantidad_mqnas = request.POST['cantidad']
    precio_mqnas = request.POST['precio']
    codigo_mqnas = request.POST ['cod_maquina']
    diseno_mqnas = request.POST['disenomaq']
    estruc_mqnas = request.POST ['estructuramaq']

    y = activo.objects.create(id_activo = id_mqnas , nombre_activo = nombre_mqnas , cantidad = cantidad_mqnas , precio = precio_mqnas)
    maquinaria.objects.create(cod_maquinaria = codigo_mqnas,diseño_maquinaria = diseno_mqnas, material_estructura = estruc_mqnas, activo = y)

    return render(request, 'respuestahtas.html',{"mensaje": mensaje})

def actualizarmaq(request):
    return render(request,"actualizarmaquina.html")

def actualizarherr(request):
    return render(request,"actualizarherramientas.html")

def editarmaq(request):
    maq = None
    mensaje = ""
    try:
        maq = maquinaria.objects.get(activo = request.GET["idactivo"])
        act = activo.objects.get(id_activo = request.GET["idactivo"])
        return render(request, "actualizarmaquina.html", {"maqui":maq, "acti":act})
    except:
        maq = None
    
    if maq == None:
        id_activo = None
        try:
            id_activo = request.POST["id_activo"]
        except:
            id_activo = None

        if id_activo != None:
            maq = maquinaria.objects.get(activo = id_activo)
            act = activo.objects.get(id_activo = id_activo)

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


            return render(request, "actualizarmaquina.html", {"mensaje":mensaje})
        
        else:
            mensaje = "No se ha encontrado la maquina"

            return render(request, "actualizarmaquina.html", {"mensaje":mensaje})
    else:
        mensaje = "No se encontró la maquina"

        return render(request, "actualizarmaquina.html", {"mensaje":mensaje})
           
def editarherr(request):
    herr = None
    mensaje = ""
    try:
        herr = herramientas.objects.get(activo = request.GET["idactivo"])
        act = activo.objects.get(id_activo = request.GET["idactivo"])
        return render(request, "actualizarherramientas.html", {"herra":herr, "acti":act})
    except:
        herr = None
    
    if herr == None:
        id_activo = None
        try:
            id_activo = request.POST["id_activo"]
        except:
            id_activo = None

        if id_activo != None:
            herr = herramientas.objects.get(activo = id_activo)
            act = activo.objects.get(id_activo = id_activo)

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


            return render(request, "actualizarherramientas.html", {"mensaje":mensaje})
        
        else:
            mensaje = "No se ha encontrado la herramienta"

            return render(request, "actualizarherramientas.html", {"mensaje":mensaje})
    else:
        mensaje = "No se encontró la herramienta"

        return render(request, "actualizarherramientas.html", {"mensaje":mensaje})
            
def respuestaherramientas(request):
    return render(request, "respuestaherramientas.html")

def crearclientes(request):

    return render(request, 'crearclientes.html')

def registrarCliente(request):

    mensaje = "Se creo Ok"
    rut_clte = request.POST['rut_cliente']
    nombre_clte= request.POST['nombre_cliente']
    telefono_clt = request.POST['telefono_contacto']
    direccion_clte = request.POST['direccion']
    maqui = request.POST['cod_maquina']
    z = maquinaria.objects.get(activo__maquinaria__cod_maquinaria = maqui)

    clientes.objects.create(rut_cliente = rut_clte, nombre_cliente = nombre_clte, telefono_contacto =telefono_clt, direccion = direccion_clte, maquinaria = z)
    return render(request, 'respuestaHtas.html',{"mensaje": mensaje})

def crearusuarios(request):
    
    return render (request, 'crearusuarios.html')

def registrarUsuario(request):

    mensaje = "Se creo Ok"
    id_usrio = request.POST['id_us']
    p_nombre_usrio = request.POST['primer_nombre']
    s_nombre_usrio = request.POST['segundo_nombre']
    p_apellido_usrio = request.POST['primer_apellido']
    s_apellido_usrio = request.POST['segundo_apellido']
    email_usrio = request.POST['email']
    telefono_usrio = request.POST['nro_telefono']
    psw_usrio = request.POST['psw']
    fecha_nacimiento_usrio = request.POST['fecha_nacimiento']
    rolusrio = request.POST['rol']
    w = roles.objects.get(roles__nombre_rol = rolusrio)

    personas.objects.create(us_id = id_usrio, primer_nombre = p_nombre_usrio, segundo_nombre = s_nombre_usrio, 
    primer_apellido = p_apellido_usrio, segundo_apellido = s_apellido_usrio, email = email_usrio,
    nro_telefono = telefono_usrio , psw = psw_usrio , fecha_nacimiento = fecha_nacimiento_usrio, roles = w)    
    return render(request, 'respuestaHtas.html',  {"mensaje": mensaje})

def listarherramientas(request):

    x = herramientas.objects.select_related ('activo').all()

    return render(request,"listarherramientas.html", {'herramientas':x})

def listarmaquinaria(request):

    y = maquinaria.objects.select_related ('activo').all()

    return render(request,"listarmaquinaria.html", {'maquinaria': y})

def listarclientes(request):

    z = clientes.objects.select_related ('maquinaria').all()

    return render(request,"listarclientes.html", {'clientes': z})

### Se integra informacion de inicion de sesion 
#Considerar que, si se crea el usuario en roles_permisos para iniciar sesion en el login.... no permite realizar ingresos de maquinarias/htas/clientes en la BD
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