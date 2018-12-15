from apps.Usuario.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.Index.models import Cliente,AsignarTecnicos

class RegistroForm(UserCreationForm):

	class Meta:
		model = User

		fields = {
		'username',
		'first_name',
		'last_name',
		'email',
		}
		labels = {
		'username': 'Nombre de usuario',
		'first_name': 'Nombre',
		'last_name': 'Apellido',
		'email': 'Correo',
		}

class CrearCliente(forms.ModelForm):
	class Meta:
		model = Cliente

		fields = [
		'nombre',
		'direccion',
		'ciudad',
		'comuna',
		'telefono',
		'correo',
		]

		labels = {
		'nombre': 'Nombres',
		'direccion': 'Direccion',
		'ciudad': 'Ciudad',
		'comuna': 'Comuna',
		'telefono': 'Telefono',
		'correo': 'Correo',

		}

		widgets = {
		'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'direccion': forms.TextInput(attrs={'class':'form-control'}),
		'ciudad': forms.TextInput(attrs={'class':'form-control'}),
		'comuna': forms.TextInput(attrs={'class':'form-control'}),
		'telefono': forms.TextInput(attrs={'class':'form-control'}),
		'correo': forms.EmailInput(attrs={'class':'form-control'}),
		}


class AsignarTecnico(forms.ModelForm):
	class Meta:
		model = AsignarTecnicos

		fields = [
		'nombre',
		'direccion',
		'ciudad',
		'comuna',
		'telefono',
		'correo',
		'usuario',
		]

		labels = {
		'nombre': 'Nombres',
		'direccion': 'Direccion',
		'ciudad': 'Ciudad',
		'comuna': 'Comuna',
		'telefono': 'Telefono',
		'correo': 'Correo',
		'usuario': 'Tecnico',
		}

		widgets = {
		'nombre': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
		'direccion': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
		'ciudad': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
		'comuna': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
		'telefono': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
		'correo': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
		'Usuario': forms.Select(attrs={'class':'form-control'}),
		}