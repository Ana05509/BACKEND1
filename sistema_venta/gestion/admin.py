from django.contrib import admin
from .models import Empleados

@admin.register (Empleados)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'direccion', 'email','telefono','cargo')
    search_fields = ('cedula', 'nombre', 'apellido') #Se agrega la busqueda por cedula y apellido
    list_filter = ('cedula', 'apellido') #Se agrega filtro por cedula y apellido



