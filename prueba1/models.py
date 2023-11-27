from django.db import models
from django.contrib.auth.models import Group
Group.objects.get_or_create(name='Cajero')
Group.objects.get_or_create(name='Estudiante')
# Create your models here.
# Modelo para la tabla de Proveedores.
class Proveedores(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=8)
    def __str__(self):
        return self.nombre
# Modelo para la tabla de productos.
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    fk_prov=models.ForeignKey(Proveedores, on_delete=models.CASCADE) # Se relacionará con el id de la tabla Proveedores
    def __str__(self):
        return self.nombre