from apps.Usuario.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.Trabajador.models import RealizaOrden

class AsignarTecnico(forms.ModelForm):
	class Meta:
		model = RealizaOrden

		fields = [
		'nombre',
		'fecha',
		'horainicio',
		'horafin',
		'modeloascensor',
		'fallasdetectadas',
		'cambiopiezas',
		'reparacionesefectuadas',
		]

		labels = {
		'nombre' : 'Nombre del cliente',
		'fecha' : 'Fecha de atencion',
		'horainicio' : 'Hora de inicio',
		'horafin' : 'Hora de termino',
		'modeloascensor' : 'Modelo de Ascensor',
		'fallasdetectadas' : 'Fallas Detectadas',
		'cambiopiezas' : 'Piezas Cambiadas',
		'reparacionesefectuadas' : 'Reparaciones efectuadas',
		}

		widgets = {
		'nombre': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
		'fecha' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'horainicio': forms.TextInput(attrs={'class':'form-control','type':'time'}),
		'horafin': forms.TextInput(attrs={'class':'form-control','type':'time'}),
		'modeloascensor': forms.TextInput(attrs={'class':'form-control'}),
		'fallasdetectadas': forms.Textarea(attrs={'class':'form-control'}),
		'cambiopiezas': forms.Textarea(attrs={'class':'form-control'}),
		'reparacionesefectuadas': forms.Textarea(attrs={'class':'form-control'}),
		}