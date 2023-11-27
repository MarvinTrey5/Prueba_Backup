from django import forms
# Clase para añadir productos
# y se llama en la view.py 
class Add_prod(forms.Form):
    nombre = forms.CharField(max_length=100)
    stock = forms.IntegerField()
    fk_prov=forms.IntegerField() # Llave foránea que se relaciona con el id de la tabla Proveedor.