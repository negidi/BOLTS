from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import activo
from .models import herramientas
from .models import maquinaria
from .models import Usuario
from .models import clientes
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime

from inventario.forms import FormularioRegistrar
# Create your views here.

def login_request(request) :
    if request.user.is_authenticated: 
         ##si el usuario esta autenticado redirige##
        return redirect("/home")
    
        
    mensaje = ""
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasenna = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contrasenna)
            if user is not None:
                login(request, user)  # para loguear al usuario#
                messages.info(request, f"{usuario} logueado")
                return redirect("/")
            else:
                mensaje = "Error de usuario o contraseña"
                messages.error(request, "Error de usuario o contraseña")
        else:
            mensaje = "Error de usuario o contraseña"
            messages.error(request, "Error de usuario o contraseña")
    return render(request, "registration/login.html", {"mensaje": mensaje})

def listarusuario(request):
    x = Usuario.objects.all()
    return render(request,"listarusuario.html", {"usuario" : x})

def signup(request):
    mensaje = ""
    if request.method == "POST":
        form = FormularioRegistrar(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            mensaje = "Usuario creado correctamente"
        else:
            mensaje = "Favor validar contraseña, considerar el largo de 8 caracteres y no ingresar contraseñas anteriores"
    else:
        form = FormularioRegistrar()

    return render(request, "registration/signup.html", {"form": form, "mensaje": mensaje})

def logout_request(request):
    logout(request)
    return redirect("/auth/login_request")

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def creacionActivo(request):

    return render(request, 'creacionActivo.html')

def crearHerramientas(request):
    id_activo_automatic = str((herramientas.objects.all().count() + 1)  * 7)
    idid = "herr" +  id_activo_automatic
    return render(request, 'crearHerramientas.html',{'idid':idid})

def registrarHerramienta(request):

    id_activo_automatic = str((herramientas.objects.all().count() + 1)  * 7)
    idid = "herr" +  id_activo_automatic
    mensaje = "Herramienta ingresada correctamente"
    nombre_herramientas = request.POST['nombre_activo']
    cantidad_herramientas = request.POST['cantidad']
    precio_herramientas = request.POST['precio']
    proveedor_herramientas = request.POST['proveedor']
    marca_herramientas = request.POST ['marca']
    estado_herramienta = request.POST['estado']
    
    x = activo.objects.create(id_activo = idid , nombre_activo = nombre_herramientas , cantidad = cantidad_herramientas , precio = precio_herramientas, estado = estado_herramienta)
    herramientas.objects.create(proveedor = proveedor_herramientas, marca = marca_herramientas, activo = x)

    return render(request, 'respuestaHtas.html',{"mensaje": mensaje})

def crearMaquinaria(request):

    id_activo_automatic = str((maquinaria.objects.all().count() + 1)  * 7)
    idid = "maqu" +  id_activo_automatic

    return render(request, 'crearMaquinaria.html',{'idid':idid})

def registrarMaquinaria(request):

    id_activo_automatic = str((maquinaria.objects.all().count() + 1)  * 7)
    idid = "maqu" +  id_activo_automatic
    mensaje = "Maquinaria ingresada correctamente"
    nombre_mqnas = request.POST['nombre_activo']
    cantidad_mqnas = request.POST['cantidad']
    precio_mqnas = request.POST['precio']
    diseno_mqnas = request.POST['disenomaq']
    estruc_mqnas = request.POST ['estructuramaq']
    estado_mqnas = request.POST['estado']


    y = activo.objects.create(id_activo = idid , nombre_activo = nombre_mqnas , cantidad = cantidad_mqnas , precio = precio_mqnas, estado = estado_mqnas)
    maquinaria.objects.create(diseño_maquinaria = diseno_mqnas, material_estructura = estruc_mqnas, activo = y)

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
            estado_a = request.POST["estado"]
            disenomaq_a = request.POST["disenomaq"]
            estructuramaq_a = request.POST["estructuramaq"]
            act.nombre_activo = nombre_a
            act.cantidad = cantidad_a
            act.precio = precio_a
            act.estado = estado_a
            maq.diseño_maquinaria = disenomaq_a
            maq.material_estructura = estructuramaq_a
            

            try:
                act.save()
                maq.save()
                mensaje = "Maquina actualizada con exito"
            except:
                mensaje = "Ha ocurrido un error al actualizar"


            return render(request, "actualizarmaquina.html", {"mensaje":mensaje})
        
        else:
            mensaje = "No se ha encontrado la maquina ingresada"

            return render(request, "actualizarmaquina.html", {"mensaje":mensaje})
    else:
        mensaje = "No se encontró la maquina ingresada"

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
            estado_a = request.POST["estado"]
            proveedorherr_a = request.POST["proveedorherr"]
            marcaherr_a = request.POST["marcaherr"]
            act.nombre_activo = nombre_a
            act.cantidad = cantidad_a
            act.precio = precio_a
            act.estado = estado_a
            herr.proveedor = proveedorherr_a
            herr.marca = marcaherr_a
            

            try:
                act.save()
                herr.save()
                mensaje = "Herramienta actualizada con exito"
            except:
                mensaje = "Ha ocurrido un error al actualizar la herramienta"


            return render(request, "actualizarherramientas.html", {"mensaje":mensaje})
        
        else:
            mensaje = "No se ha encontrado la herramienta ingresada"

            return render(request, "actualizarherramientas.html", {"mensaje":mensaje})
    else:
        mensaje = "No se encontró la herramienta ingresada"

        return render(request, "actualizarherramientas.html", {"mensaje":mensaje})
            
def respuestaherramientas(request):
    return render(request, "respuestaherramientas.html")

def crearclientes(request):
    id_activo_automatic = str((clientes.objects.all().count() + 1)  * 7)
    idco = "idco" +  id_activo_automatic
    y = maquinaria.objects.all()
    return render(request,"crearClientes.html",{'y': y, 'idco':idco})

def registrarCliente(request):
    id_activo_automatic = str((clientes.objects.all().count() + 1)  * 7)
    idco = "idco" +  id_activo_automatic
    mensaje = "Cliente ingresado correctamente"
    rut_clte = request.POST['rut_cliente']
    nombre_clte= request.POST['nombre_cliente']
    telefono_clt = request.POST['telefono_contacto']
    direccion_clte = request.POST['direccion']
    unidad = request.POST['unidades']
    fecha = request.POST['fecha']
    maqui = request.POST['cod_maquina']
    z = maquinaria.objects.get(activo__maquinaria__activo = maqui)
    total = int(unidad) * int(z.activo.precio)
    clientes.objects.create(id_compra = idco,rut_cliente = rut_clte, nombre_cliente = nombre_clte, telefono_contacto =telefono_clt, direccion = direccion_clte, unidades = unidad, fecha = fecha ,maquinaria = z,total = total)

    return render(request, 'respuestaHtas.html',{"mensaje": mensaje})

def listarherramientas(request):

    x = herramientas.objects.select_related ('activo').all()
    p = herramientas.objects.all()
    return render(request,"listarherramientas.html", {'herramientas':x, "p" : p})

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


def filtroherr(request):
    if request.GET["nombre_activ"] and request.GET["prec"] and request.GET["provee"]: # valida por nombre y precio y proveedor (variacion en los precios.)
        prov = request.GET["provee"]
        htas = request.GET["nombre_activ"]
        if request.GET["validar"] == 'pmayor':
            prec = request.GET["prec"]
            y = herramientas.objects.filter(activo__precio__gt=prec, activo__nombre_activo__iexact=htas, proveedor__iexact=prov)
        elif request.GET["validar"] == 'pmenor':
            prec = request.GET["prec"]
            y = herramientas.objects.filter(activo__precio__lt=prec, activo__nombre_activo__iexact=htas, proveedor__iexact=prov)
        elif request.GET["validar"] == 'pigual':
            prec = request.GET["prec"]
            y = herramientas.objects.filter(activo__precio__exact=prec, activo__nombre_activo__iexact=htas, proveedor__iexact=prov)
        p = herramientas.objects.all()
        return render(request,"listarherramientas.html",{"fullhtas": y,"query":prec,'p':p})
    
    elif request.GET["nombre_activ"] and request.GET["prec"]: # valida por nombre y precio(variable)
        htas = request.GET["nombre_activ"]
        if request.GET["validar"] == 'pmayor':
                prec = request.GET["prec"]
                y = herramientas.objects.filter(activo__precio__gt=prec,activo__nombre_activo__iexact=htas)
        elif request.GET["validar"] == 'pmenor':
            prec = request.GET["prec"]
            y = herramientas.objects.filter(activo__precio__lt=prec,activo__nombre_activo__iexact=htas)
        elif request.GET["validar"] == 'pigual':
            prec = request.GET["prec"]
            y = herramientas.objects.filter(activo__precio__exact=prec,activo__nombre_activo__iexact=htas)
        p = herramientas.objects.all()
        return render(request,"listarherramientas.html",{"fullhtas": y,"query":prec,'p':p})
    
    elif request.GET["nombre_activ"] and request.GET["provee"]: # valida por nombre y proveedor
        htas = request.GET["nombre_activ"]
        prov = request.GET["provee"]
        p = herramientas.objects.all()
        y = herramientas.objects.filter(activo__nombre_activo__iexact = htas , proveedor__iexact=prov)
        return render(request,"listarherramientas.html",{"fullhtas": y,'p':p})
    
    elif request.GET["prec"] and request.GET["provee"]: # valida por precio y proveedor
        prov = request.GET["provee"]
        prec = request.GET["prec"]
        p = herramientas.objects.all()
        y = herramientas.objects.filter(activo__precio__exact=prec, proveedor__iexact=prov)
        return render(request,"listarherramientas.html",{"fullhtas": y,"query":prec,'p':p})
    
    elif request.GET["nombre_activ"]: # valida el nombre del activo
        htas = request.GET["nombre_activ"]
        p = herramientas.objects.all()
        x = herramientas.objects.filter(activo__nombre_activo__icontains=htas)
        
        return render(request,"listarherramientas.html",{"fullhtas": x,"query":htas,'p':p})
    elif request.GET["provee"] != '': # valida el nombre del activo
        htas = request.GET["provee"]
        x = herramientas.objects.filter(proveedor__iexact=htas)
        p = herramientas.objects.all()
        return render(request,"listarherramientas.html",{"fullhtas": x,"query":htas, 'p':p})
  
    elif request.GET["prec"]: #Valida el precio mayor, menor o igual.
        if request.GET["validar"] == 'pmayor':
                prec = request.GET["prec"]
                x = herramientas.objects.filter(activo__precio__gt=prec)
                return render(request,"listarherramientas.html",{"fullhtas": x,"query":prec})
        elif request.GET["validar"] == 'pmenor':
            prec = request.GET["prec"]
            x = herramientas.objects.filter(activo__precio__lt=prec)
            return render(request,"listarherramientas.html",{"fullhtas": x,"query":prec})
        elif request.GET["validar"] == 'pigual':
            prec = request.GET["prec"]
            x = herramientas.objects.filter(activo__precio__exact=prec)
            return render(request,"listarherramientas.html",{"fullhtas": x,"query":prec}) 
    else:
        mensaje = "Debe ingresar un nombre de herramienta"
        return render(request,"listarherramientas.html",{"mensaje": mensaje})
        
def filtromaqu(request):
    if request.GET["nombre_activ"] and request.GET["prec"]: # valida por nombre y precio(exacto)
        htas = request.GET["nombre_activ"]
        if request.GET["validar"] == 'pmayor':
            prec = request.GET["prec"]
            x = maquinaria.objects.filter(activo__precio__gt=prec, activo__nombre_activo__iexact=htas)
        elif request.GET["validar"] == 'pmenor':
            prec = request.GET["prec"]
            x = maquinaria.objects.filter(activo__precio__lt=prec, activo__nombre_activo__iexact=htas)
        elif request.GET["validar"] == 'pigual':
            prec = request.GET["prec"]
            x = maquinaria.objects.filter(activo__precio__exact=prec, activo__nombre_activo__iexact=htas)
        return render(request,"listarmaquinaria.html",{"fullhtas": x,"query":prec})
    elif request.GET["nombre_activ"]: # valida el nombre del activo
        htas = request.GET["nombre_activ"]
        x = maquinaria.objects.filter(activo__nombre_activo__iexact=htas)
        return render(request,"listarmaquinaria.html",{"fullhtas": x,"query":htas})
    elif request.GET["prec"]: #Valida el precio mayor, menor o igual.
        if request.GET["validar"] == 'pmayor':
            prec = request.GET["prec"]
            x = maquinaria.objects.filter(activo__precio__gt=prec)
            return render(request,"listarmaquinaria.html",{"fullhtas": x,"query":prec})
        elif request.GET["validar"] == 'pmenor':
            prec = request.GET["prec"]
            x = maquinaria.objects.filter(activo__precio__lt=prec)
            return render(request,"listarmaquinaria.html",{"fullhtas": x,"query":prec})
        elif request.GET["validar"] == 'pigual':
            prec = request.GET["prec"]
            x = maquinaria.objects.filter(activo__precio__exact=prec)
            return render(request,"listarmaquinaria.html",{"fullhtas": x,"query":prec}) 
    

    else:
        mensaje = "Debe ingresar un nombre de herramienta"
        return render(request,"listarmaquinaria.html",{"mensaje": mensaje})
        
def filtroclnte(request):
    if request.GET["nombre_cliente"] and  request.GET["fecha"]: #Validando nombre de cliente y fecha de registro
        fullclientes = request.GET["nombre_cliente"] # Get nombre
        f = request.GET["fecha"]# Get fecha
        x = clientes.objects.filter(nombre_cliente__iexact= fullclientes, fecha = f) #Busqueda en BD
        w=x.count() #Contador de resgistros para el cliente buscado
        return render(request,"listarclientes.html",{"fullclte": x,"query":fullclientes, "contador": w})
    elif request.GET["nombre_cliente"]:
        fullclientes = request.GET["nombre_cliente"] # Get nombre
        x = clientes.objects.filter(nombre_cliente__iexact = fullclientes) #comparacion del nombre ingresado
        w=x.count() #Contador de resgistros para el cliente buscado
        return render(request, "listarclientes.html", {"fullclte" : x,"query":fullclientes, "contador": w})
    elif request.GET["fecha"]: #validar comparacion de fechas 
        if request.GET["validar"] == 'figual':
            f = request.GET["fecha"]# Fecha igual
            x = clientes.objects.filter(fecha__exact = f) 
            w=x.count() #Contador de resgistros para el cliente buscado
            return render(request, "listarclientes.html", {"fullclte" : x, "contador": w})
        elif request.GET["validar"] == 'fmayor':
            f = request.GET["fecha"]# Fecha mayor a 
            x = clientes.objects.filter(fecha__gt=f) 
            w=x.count() #Contador de resgistros para el cliente buscado
            return render(request, "listarclientes.html", {"fullclte" : x, "contador": w})
        else:
            f = request.GET["fecha"]# Fecha menor a 
            x = clientes.objects.filter(fecha__lt=f) 
            w=x.count() #Contador de resgistros para el cliente buscado
            return render(request, "listarclientes.html", {"fullclte" : x, "contador": w})

    #Crear filtro por las maquinas
    #elif request.GET["cod_maquina"]:
    #    x = request.GET["cod_maquina"]
    #    y = maquinaria.objects.all()
    #    return render(request,"listarclientes.html",{"y": y, })
        
    else:
        mensaje = "Debe ingresar un nombre de Cliente"
        return render(request,"listarclientes.html",{"mensaje": mensaje})

def actualizarcliente(request):
    return render(request, 'actualizarcliente.html')

def editarclte(request): #validar 
    clte = None
    mensaje = ""
    try:
        clte = clientes.objects.get(id_compra = request.GET["idcliente"])
        y = maquinaria.objects.all()

        return render(request, "actualizarcliente.html", {"cltes" : clte, "y":y})
    except:
        clte = None

    if clte == None:
        id_compra = None
        try:
            id_compra = request.POST["id_compra"]
        except:
            id_compra = None

        if id_compra != None:
            clte = clientes.objects.get(id_compra = id_compra)

            rut_clt = request.POST["rut_cliente"]
            nombre_clt = request.POST["nombre_cliente"]
            telefono_clt = request.POST["telefono_contacto"]
            direccion_clt = request.POST["direccion"] 
            unidades_clt = request.POST["unidades"]
            fecha_clt = datetime.now()
            total_clt = request.POST ["total"]
            maqui = request.POST['cod_maquina']
            z = maquinaria.objects.get(activo__maquinaria__activo = maqui)
            y = maquinaria.objects.all()
            
            clte.rut_cliente = rut_clt
            clte.nombre_cliente = nombre_clt
            clte.telefono_contacto = telefono_clt
            clte.direccion = direccion_clt
            clte.unidades = unidades_clt
            clte.fecha = fecha_clt
            clte.total = total_clt
            clte.maquinaria = z

            try:
                clte.save()
                mensaje = "Se ha actualizado el cliente"
            except:
                mensaje = "Ha ocurrido un error al actualizar el cliente"
            
            return render(request, "actualizarcliente.html", {"mensaje":mensaje,"y" : y })
        else:
            mensaje = "No se ha encontrado el registro consultado"

            return render(request, "actualizarcliente.html", {"mensaje":mensaje, "y": y})
    else:
        mensaje = "No se encontró el registro consultado"

        return render(request, "actualizarcliente.html", {"mensaje":mensaje})
                
def actualizarusuario(request):
    return render(request,"actualizarusuario.html")

def editarus(request):
    us = None
    mensaje = ""

    try:
        us = Usuario.objects.get(username= request.GET["username"])
        return render(request, "actualizarusuario.html", {"us":us})

    except: 
        us = None
    
    if us == None:
        username = None
        try:
            username = request.POST["username"]
        except:
            username = None

        if username != None:
            us = Usuario.objects.get(username = username)

            nombres_a = request.POST["nombre_usuario"]
            apellidos_a = request.POST["primer_apellido"]
            rut_a = request.POST["rut_usuario"]
            email_a = request.POST["email_usuario"]
            rol_a = request.POST["rol"]

            Usuario.first_name = nombres_a
            Usuario.last_name= apellidos_a
            Usuario.rut= rut_a
            Usuario.email = email_a
            ##telefono_usuario = request.POST["telefono_usuario "]##
            Usuario.rol = rol_a
            try:
                us.save()
                mensaje = "Se ha actualizado el usuario"
            except:
                mensaje = "Ha ocurrido un error al actualizar"


            return render(request, "actualizarusuario.html", {"mensaje":mensaje})
        
        else:
            mensaje = "No se encontro el usuario ingresado"

            return render(request, "actualizarusuario.html", {"mensaje":mensaje})
    else:
        mensaje = "No se encontró usuario"

        return render(request, "actualizarusuario.html", {"mensaje":mensaje})