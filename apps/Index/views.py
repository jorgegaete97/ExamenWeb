from django.http import HttpResponse
from apps.Usuario.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.Index.forms import RegistroForm,CrearCliente,AsignarTecnico
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.Index.models import Cliente,AsignarTecnicos

# Create your views here.


def index(request):
	return render(request, 'Empresa/index.html')


class RegistroUsuario(CreateView):
	model = User
	template_name = "Empresa/registrarse.html"
	form_class = RegistroForm
	success_url = reverse_lazy('login')


@login_required
def home(request):
    return render(request, 'Empresa/index.html')


def Cliente_List(request):
	cliente = Cliente.objects.all()
	contexto = {'clientes':cliente}
	return render(request,'Empresa/clientes.html',contexto)


def Cliente_List2(request):
	cliente = Cliente.objects.all()
	contexto = {'clientes':cliente}
	return render(request,'Empresa/asignaciones.html',contexto)


def formulario_view(request):
	if request.method == 'POST':
		form = CrearCliente(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index:Menu')
	else:
		form = CrearCliente()

	return render(request, 'Empresa/registrar_cliente.html',{'form':form})


def EditarCliente(request, id):
	cliente = Cliente.objects.get(id = id)
	if request.method == 'GET':
		form = CrearCliente(instance=cliente)
	else:
		form = CrearCliente(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
		return redirect('index:Menu')
	return render(request, 'Empresa/registrar_cliente.html',{'form': form})

def EliminarCliente(request, id):
	cliente = Cliente.objects.get(id = id)
	if request.method == 'POST':
		cliente.delete()
		return redirect('index:Menu')
	return render(request, 'Empresa/eliminar_cliente.html',{'cliente': cliente})


def AsignarTecnicoU(request, id):
	cliente = Cliente.objects.get(id = id)
	if request.method == 'GET':
		form = AsignarTecnico(instance=cliente)
	else:
		form = AsignarTecnico(request.POST, instance=cliente)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			direccion = form.cleaned_data['direccion']
			ciudad = form.cleaned_data['ciudad']
			comuna = form.cleaned_data['comuna']
			telefono = form.cleaned_data['telefono']
			correo = form.cleaned_data['correo']
			id_cliente = cliente.id
			usuario = form.cleaned_data['usuario']
			AsignarTecnicos.objects.create(nombre=nombre,direccion=direccion,ciudad=ciudad,comuna=comuna,telefono=telefono,correo=correo,id_cliente=id_cliente,usuario=usuario)
			form.save()
		return redirect('index:Menu')
	return render(request, 'Empresa/asignar_tecnico.html',{'form': form})