from django import forms
from AppHiTure.models import Cliente, Venta, Venta_producto, Producto, Genero_producto, Comprobante_pago, Tipo_pago 
from django.forms import ModelForm
#Para el formulario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Este es para el usuario común
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'rut_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Rut'
                }
            ),
            'nombre_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre'
                }
            ),
            'apellido_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Apellido Paterno'
                }
            ),
            'mail_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Dirección'
                }
            ),
            'direccion_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Correo'
                }
            ),
            'telefono_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Teléfono'
                }
            ),
            'usuario_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Usuario'
                }
            ),
            'password_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Contraseña'
                }
            ),
        }


#Este es para el producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre_producto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre del Producto'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Precio del Producto'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Descripción'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Dirección',
                    'type': 'number',
                    'min': '0',
                }
            ),
            #'genero_producto': forms.TextInput(
            #    attrs={
            #        'class': 'form-control',
            #        'placeholder': 'Ingrese el Género'
            #    }
            #),
        }


#Este será para el administrador
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
#        widgets = {
#            'first_name': forms.TextInput(
#                attrs={
#                    'class': 'form-control',
#                    'placeholder': 'Ingrese su Nombre'
#                }
#            ),
#            'username': forms.TextInput(
#                attrs={
#                    'class': 'form-control',
#                    'placeholder': 'Ingrese su Apellido'
#                }
#            ),
#            'username': forms.TextInput(
#                attrs={
#                    'class': 'form-control',
#                    'placeholder': 'Ingrese un Usuario'
#                }
#            ),
#            'email': forms.TextInput(
#                attrs={
#                    'class': 'form-control',
#                    'placeholder': 'Ingrese un Correo'
#                }
#            ),
#            'password1': forms.TextInput(
#                attrs={
#                    'class': 'form-control',
#                    'placeholder': 'Ingrese una Contraseña'
#                }
#            )
#            'password2': forms.TextInput(
#                attrs={
#                    'class': 'form-control',
#                    'placeholder': 'Ingrese Nuevamente la Contraseña'
#                }
#            )
#        }