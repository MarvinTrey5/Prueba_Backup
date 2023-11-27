from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Clase para acceder al login obteniendo
# su usuario y su contraseña.
# y se llama en la views.py
class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']