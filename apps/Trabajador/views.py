from django.shortcuts import render
from apps.Index.models import AsignarTecnicos
from django.shortcuts import render
from apps.Index.models import Cliente
from apps.Trabajador.models import RealizaOrden
from apps.Trabajador.forms import AsignarTecnico
from django.shortcuts import render, redirect
# Create your views here.


def VerClientes(request):
	Usuario = request.user
	info = AsignarTecnicos.objects.filter(usuario_id=Usuario.id)
	contexto = {'Info': info}
	return render(request, 'Empresa/ver_clientes.html', contexto)


def RealizarOrden(request, id):
	cliente = AsignarTecnicos.objects.get(id = id)
	Usuario = request.user
	if request.method == 'GET':
		form = AsignarTecnico(instance=cliente)
	else:
		form = AsignarTecnico(request.POST, instance=cliente)

		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			fecha = form.cleaned_data['fecha']
			horainicio = form.cleaned_data['horainicio']
			horafin = form.cleaned_data['horafin']
			modeloascensor = form.cleaned_data['modeloascensor']
			fallasdetectadas = form.cleaned_data['fallasdetectadas']
			reparacionesefectuadas = form.cleaned_data['reparacionesefectuadas']
			cambiopiezas = form.cleaned_data['cambiopiezas']
			usuario = Usuario
			RealizaOrden.objects.create(nombre=nombre,fecha=fecha,horainicio=horainicio,horafin=horafin,modeloascensor=modeloascensor,
				fallasdetectadas=fallasdetectadas,reparacionesefectuadas=reparacionesefectuadas,cambiopiezas=cambiopiezas,usuario=Usuario)
			form.save()
		return redirect('index:Menu')
	return render(request, 'Empresa/orden.html',{'form': form})


def VerOrdenes(request):
	Usuario = request.user
	info = RealizaOrden.objects.filter(usuario_id=Usuario.id)
	contexto = {'Info': info}
	return render(request, 'Empresa/ordenes_realizadas.html', contexto)