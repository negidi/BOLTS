from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import activo,herramientas, maquinaria,clientes, Usuario


# Register your models here.

class herramientasresources(resources.ModelResource):
    fields = (
    'activo',
    'proveedor',
    'marca',
    )
    class Meta:
        model = herramientas


class clientesresources(resources.ModelResource):
    fields = (
    'id_compra',   
    'rut_cliente',
    'nombre_cliente',
    'telefono_contacto',
    'direccion',
    'fecha',
    'total',
    'activo',
    'maquinaria',
    )
    class Meta:
        model = clientes

class activoresources(resources.ModelResource):
    fields = (
    'id_activo',
    'nombre_activo',
    'cantidad',
    'precio',
    'activo',
    'estado',
    )
    class Meta:
        model = activo

@admin.register(herramientas)
class herramientaAdmin(ImportExportModelAdmin):
    resource_class = herramientasresources
    list_display = (
    'activo',
    'proveedor',
    'marca',
    )

@admin.register(activo)
class activoAdmin(ImportExportModelAdmin):
    list_display = (
    'id_activo',
    'nombre_activo',
    'cantidad',
    'precio',
    'activo',
    'estado',
    )

    search_fields = ('id_activo',)
    list_filter = ('nombre_activo',)

@admin.register(maquinaria)
class maquinariaAdmin(admin.ModelAdmin):
    list_display = (
    'activo',   
    'diseño_maquinaria',
    'material_estructura',
    )

@admin.register(clientes)
class clientesAdmin(ImportExportModelAdmin):
    list_display = (
    'id_compra',   
    'rut_cliente',
    'nombre_cliente',
    'telefono_contacto',
    'direccion',
    'fecha',
    'total',
    'activo',
    'maquinaria',
    )

class usuarioresources(resources.ModelResource):
 fields = (
 'rut',
 'first_name',
 'last_name',
 'email',
 'rol',
 'is_active',
 'username',
 )
 class Meta:
     model = Usuario

@admin.register(Usuario)
class herramientaAdmin(ImportExportModelAdmin):
 resource_class = usuarioresources
 list_display = (
 'rut',
 'first_name',
 'last_name',
 'email',
 'rol',
 'is_active',
 'username',
 )



    
