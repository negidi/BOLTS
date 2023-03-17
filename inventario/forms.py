from django import forms
from django.contrib.auth.forms import UserCreationForm
from inventario.models import Usuario


class FormularioRegistrar(UserCreationForm):
    rut = forms.CharField(max_length=12)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    

    class Meta:
        model = Usuario
        fields = ("username", "rut", "rol", "first_name", "last_name", "email")
