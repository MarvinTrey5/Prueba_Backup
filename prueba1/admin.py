from django.contrib import admin
from .models import Proveedores,Productos
# Register your models here.
# Para poder visualizar los datos al ingresar como pgAdmin
admin.site.register(Proveedores)
admin.site.register(Productos)