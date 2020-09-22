from django import forms
from django.forms import ModelForm
from .models import Cliente, Planes, Contrato, Cupon
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'password', 'dni', 'direccion', 'ciudad', 'codigo_postal', 'provincia']

        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre completo del cliente',
                    'id': 'nombre'
                }),
            'email' : forms.EmailInput(
                attrs={
                    
                    'class': 'form-control',
                    'placeholder': 'ejemplo@mail.com',
                    'id': 'email'
                }),
            'telefono' : forms.NumberInput(
                attrs={

                    'class': 'form-control',
                    'placeholder': '12345678',
                    'id': 'telefono'
                }),
            'password' : forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '********',
                    'id': 'password'
                }),
            'dni' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'dni',
                    'id': 'dni'
                }),
            'direccion' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección',
                    'id': 'direccion'
                }),
            'ciudad' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la ciudad',
                    'id': 'ciudad'
                }),
            'codigo_postal' : forms.NumberInput(
                attrs={

                    'class': 'form-control',
                    'placeholder': 'Codigo postal',
                    'id': 'codigo_postal'
                }),
            'provincia' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la provincia',
                    'id': 'provincia'
                }),
            
        }

class PlanesForm(ModelForm):
    
    class Meta:
        model = Planes
        fields = ['nombre', 'vel_subida', 'vel_bajada', 'precio', 'detalle']
        labels = {
            'nombre': 'Nombre',
            'vel_subida': 'Velocidad de Subida',
            'vel_bajada': 'Velocidad de Bajada',
            'precio': 'Precio',
            'detalle': 'Detalle',
        }
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del plan',
                    'id': 'nombre'
                }),
            'vel_subida' : forms.NumberInput(
                attrs={
                    
                    'class': 'form-control',
                    'placeholder': 'Kbps',
                    'id': 'vel_subida'
                }),
            'vel_bajada' : forms.NumberInput(
                attrs={

                    'class': 'form-control',
                    'placeholder': 'Kbps',
                    'id': 'vel_bajada'
                }),
            'precio' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'AR $$$',
                    'id': 'precio'
                }),
            'detalle' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Detalle del Plan',
                    'id': 'detalle'
                })
            
        }


class ContratoForm(ModelForm):
    
    class Meta:
        model = Contrato
        fields = ['cliente', 'plan', 'ip', 'detalle']
        widgets = {
            'cliente' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'cliente'
                }),
            'plan' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'plan'
                }),   
            'ip' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion IP',
                    'id': 'ip'
                }), 
            'detalle' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Detalle del Contrato',
                    'id': 'detalle'
                })
         }

class CuponesForm(ModelForm):
    
    class Meta:
        model = Cupon
        fields = ['cliente', 'contrato', 'monto', 'detalle']
        widgets = {
            'cliente' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'cliente'
                }),
            'contrato' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'contrato'
                }),   
            'monto' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'monto'
                }), 
            'detalle' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Detalle del Cupon',
                    'id': 'detalle'
                })
         }

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']