from django.core.validators import RegexValidator
from django.core.validators import ValidationError
def validacion_numeros(value):
    if not value.isdigit():
        raise ValidationError("El valor debe contenir solo numeros")