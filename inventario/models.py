from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from auditlog.registry import auditlog ##para auditoria##

# Create your models here.

class Usuario(AbstractUser):
    class Rol(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        JEFE = "JEFE", "Jefe"
        OPERADOR = "OPERADOR", "Operador"

    rut = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    rol = models.CharField(max_length=50, choices=Rol.choices)


class activo(models.Model):
    id_activo = models.CharField(primary_key = True, max_length=32)
    nombre_activo = models.CharField(max_length=32)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    activos = ( 
        ('A','Activo'),
        ('I', 'Inactivo'),
    )
    activo = models.CharField(max_length= 1, choices= activos, blank=True , null=False) 
    estados = ( 
        ('S','Sin stock'),
        ('C', 'Con Stock'),
    )
    estado = models.CharField(max_length= 1, choices= estados,  blank=True ,null=False)

class herramientas(models.Model):
    proveedor = models.CharField(max_length=70)
    marca = models.CharField(max_length=100)
    activo = models.ForeignKey(activo, related_name="herramientas", blank=True, null=False, on_delete=models.CASCADE)

class maquinaria(models.Model):
    diseño_maquinaria = models.ImageField(upload_to = "diseño", null= True)
    material_estructura = models.CharField(max_length=200)
    activo = models.ForeignKey(activo, related_name="maquinaria", blank=True, null=False, on_delete=models.CASCADE)

class clientes(models.Model):
    id_compra = models.CharField(primary_key = True, max_length=50)
    rut_cliente = models.CharField(max_length=28)
    nombre_cliente = models.CharField(max_length=32)
    telefono_contacto = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    unidades = models.IntegerField()
    fecha = models.DateField()
    total = models.CharField(max_length=15)
    activos = ( #opciones
        ('A','Activo'),
        ('I', 'Inactivo'),
    )
    activo = models.CharField(max_length= 1, choices= activos, blank=True , null=False) 
    maquinaria = models.ForeignKey(maquinaria, related_name="clientes", blank=True, null=False, on_delete=models.CASCADE)

##se incluye para auditoria##
auditlog.register(clientes)
auditlog.register(maquinaria)
auditlog.register(herramientas)
auditlog.register(activo)
auditlog.register(Usuario)