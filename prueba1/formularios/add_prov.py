from django import forms
# Clase para añadir proveedor
# y se llama en la view.py 
class Add_prov(forms.Form):
    nombre=forms.CharField(max_length=100)
    telefono=forms.CharField(max_length=8)