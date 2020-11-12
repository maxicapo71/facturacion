from django import forms
from django.forms import ModelForm
from .models import Cliente, Planes, Contrato, Cupon
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.timezone import datetime


class ClienteForm(ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'dni', 'direccion', 'ciudad', 'codigo_postal', 'provincia']
        fields_required = ['nombre', 'email', 'telefono', 'dni', 'direccion', 'ciudad', 'codigo_postal', 'provincia']
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'minlength':5,
                    'maxlength':80,
                    'pattern':'[A-Za-z\ ]{5,80}',
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
            'telefono' : forms.TextInput(
                attrs={
                    'pattern':'[0-9]{5,15}',
                    'class': 'form-control',
                    'placeholder': '12345678',
                    'id': 'telefono'
                }),
            'dni' : forms.NumberInput(
                attrs={
                    
                    'class': 'form-control',
                    'placeholder': 'dni',
                    'id': 'dni'
                }),
            'direccion' : forms.TextInput(
                attrs={
                    'pattern':'[A-Za-z0-9\ ]{5,50}',
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección',
                    'id': 'direccion'
                }),
            'ciudad' : forms.TextInput(
                attrs={
                    'pattern':'[A-Za-z\ ]{3,50}',
                    'class': 'form-control',
                    'placeholder': 'Ingrese la ciudad',
                    'id': 'ciudad'
                }),
            'codigo_postal' : forms.NumberInput(
                attrs={
                    'max':9999,
                    'min':1000,
                    'class': 'form-control',
                    'placeholder': 'Codigo postal',
                    'id': 'codigo_postal'
                }),
            'provincia' : forms.TextInput(
                attrs={
                    'pattern':'[A-Za-z\ ]{3,50}',
                    'class': 'form-control',
                    'placeholder': 'Ingrese la provincia',
                    'id': 'provincia'
                }),
            
        }



class PlanesForm(ModelForm):
    
    class Meta:
        model = Planes
        fields = ['nombre', 'vel_subida', 'vel_bajada', 'precio', 'detalle']
        fields_required = ['nombre', 'vel_subida', 'vel_bajada', 'precio', 'detalle']
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
                    'minlength':3,
                    'maxlength':50,
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del plan',
                    'id': 'nombre'
                }),
            'vel_subida' : forms.NumberInput(
                attrs={
                    
                    'min':128,
                    'class': 'form-control',
                    'placeholder': 'Kbps',
                    'id': 'vel_subida'
                }),
            'vel_bajada' : forms.NumberInput(
                attrs={
                    'min':128,
                    'class': 'form-control',
                    'placeholder': 'Kbps',
                    'id': 'vel_bajada'
                }),
            'precio' : forms.NumberInput(
                attrs={
                    'min':1,
                    'class': 'form-control',
                    'placeholder': 'AR $$$',
                    'id': 'precio'
                }),
            'detalle' : forms.Textarea(
                attrs={
                    'minlength':3,
                    'maxlength':160,
                    'class': 'form-control',
                    'placeholder': 'Detalle del Plan',
                    'id': 'detalle'
                })
            
        }


class ContratoForm(ModelForm):
    
    class Meta:
        model = Contrato
        fields = ['cliente', 'plan', 'ip', 'detalle']
        fields_required = ['cliente', 'plan', 'ip', 'detalle']
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
                    'pattern':'[0-9\.]{8,15}',
                    'class': 'form-control',
                    'placeholder': 'Direccion IP',
                    'id': 'ip'
                }), 
            'detalle' : forms.Textarea(
                attrs={
                    'minlength':3,
                    'maxlength':160,
                    'class': 'form-control',
                    'placeholder': 'Detalle del Contrato',
                    'id': 'detalle'
                })
         }

class CuponesForm(ModelForm):
    
    class Meta:
        model = Cupon
        fields = ['monto', 'detalle', 'pagado', 'fecha_pago']
        fields_required = ['monto', 'detalle', 'pagado', 'fecha_pago']
        widgets = {
            
            
            'monto' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'monto',
                    'readonly': 'true'
                }), 
            'detalle' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Detalle del Cupon',
                    'id': 'detalle',
                    'readonly': 'true'
                }),
            'pagado' : forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Pagado',
                    'id': 'pagado',
                    'checked': 'true'
                }),
            'fecha_pago' : forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fecha_pago'
                    
                    
                }),
        }
   
class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class PassUserForm(UserCreationForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User
        
        fields = ['username', 'password1', 'password2']
      