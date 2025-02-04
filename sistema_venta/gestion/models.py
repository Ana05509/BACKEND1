from django.db import models
from .choices import CARGOS 
from django.core.validators import MinLengthValidator,MaxLengthValidator,MaxValueValidator,MinValueValidator
from.validadores import validacion_numeros

# Create your models here.
class Empleados (models.Model):
    cedula = models.CharField(max_length=10,primary_key=True,validators=[MinLengthValidator(10),MaxLengthValidator(10),validacion_numeros]) #Se agrega validadores de longitud
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50,verbose_name='Apellidos dd', blank=True)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    cargo = models.CharField(max_length=50,choices=CARGOS) #Se agrega la variable cargo con las opciones definidas en choices.py

    class Meta:#Clase interna que permite definir metadatos de la clase
        verbose_name = 'Empleado xx'
        verbose_name_plural = 'Empleados yy'
        db_table = 'Empleados'

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    


