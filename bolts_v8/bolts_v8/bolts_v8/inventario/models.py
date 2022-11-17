from datetime import date
from django.db import models

# Create your models here.
class roles(models.Model):
    id_rol = models.IntegerField(primary_key = True)
    nombre_rol = models.CharField(max_length=32,unique=True)

class permisos(models.Model):
    id_permisos = models.IntegerField(primary_key = True)
    nombre_permiso = models.CharField(max_length=32,unique=True)


class roles_permisos(models.Model):
    id_roles_permisos = models.IntegerField(primary_key = True)
    roles = models.ForeignKey(roles, related_name="roles_permisos", blank=True, null=True, on_delete=models.CASCADE)
    permisos = models.ForeignKey(permisos, related_name="roles_permisos", blank=True, null=True, on_delete=models.CASCADE)


class personas(models.Model):
    us_id = models.IntegerField(primary_key = True)
    primer_nombre = models.CharField(max_length=32)
    segundo_nombre = models.CharField(max_length=32, null=True, blank=True)
    primer_apellido = models.CharField(max_length=32)
    segundo_apellido = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=32,unique=True)
    nro_telefono = models.CharField(max_length=32, unique=True)
    psw = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    roles = models.ForeignKey(roles, related_name="roles", blank=True, null=False, on_delete=models.CASCADE)


class activo(models.Model):
    id_activo = models.CharField(primary_key = True, max_length=32)
    nombre_activo = models.CharField(max_length=32)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

class herramientas(models.Model):
    proveedor = models.CharField(max_length=70)
    marca = models.CharField(max_length=100)
    activo = models.ForeignKey(activo, related_name="herramientas", blank=True, null=False, on_delete=models.CASCADE)

class maquinaria(models.Model):
    diseño_maquinaria = models.FileField(max_length=70)
    material_estructura = models.CharField(max_length=200)
    activo = models.ForeignKey(activo, related_name="maquinaria", blank=True, null=False, on_delete=models.CASCADE)

class clientes(models.Model):
    id_compra = models.CharField(primary_key = True, max_length=50)
    rut_cliente = models.CharField(max_length=28)
    nombre_cliente = models.CharField(max_length=32)
    telefono_contacto = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    unidades = models.IntegerField()
    total = models.CharField(max_length=15)
    maquinaria = models.ForeignKey(maquinaria, related_name="clientes", blank=True, null=False, on_delete=models.CASCADE)


