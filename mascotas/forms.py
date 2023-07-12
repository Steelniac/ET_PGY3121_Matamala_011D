from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'precio', 'cantidad', 'imagen']
        labels = {
            'nombre': 'Nombre',
            'codigo': 'Código',
            'precio': 'Precio',
            'cantidad': 'Cantidad',
            'imagen': 'Imagen'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese nombre..',
                'id': 'nombre',
                'class': 'form-control',
            }),
            'codigo': forms.TextInput(attrs={
                'placeholder': 'Ingrese código..',
                'id': 'codigo',
                'class': 'form-control',
            }),
            'precio': forms.NumberInput(attrs={
                'placeholder': 'Ingrese precio..',
                'id': 'precio',
                'class': 'form-control',
            }),
            'cantidad': forms.NumberInput(attrs={
                'placeholder': 'Ingrese cantidad..',
                'id': 'cantidad',
                'class': 'form-control',
            }),
            'imagen': forms.FileInput(
                attrs={
                'class': 'form-control',
                'id': 'imagen',
            })
        }


