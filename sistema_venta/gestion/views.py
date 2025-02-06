

from django.shortcuts import render
from rest_framework import viewsets
from .models import Empleados
from .serializer import EmpleadosSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated #para que se accedan solo los usuarios 
#con permisos esto se agg solo para explicar borrala depues si lo usamos

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
    permission_classes = [AllowAny] 
    #Para que todos los usuarios puedan ver los empleados, 
    # si se quiere que solo los usuarios autenticados puedan verlos se cambia a IsAuthenticated
