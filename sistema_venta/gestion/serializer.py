from rest_framework import serializers
from.models import Empleados

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'  #'para todos los campos'
        
        #para llamar a todos los elemntos de los empleados

