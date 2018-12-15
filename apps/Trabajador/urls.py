from django.conf.urls import url, include
from apps.Trabajador.views import VerClientes,RealizarOrden,VerOrdenes

from django.urls import include, path

app_name = "trabajador";

urlpatterns = [
url(r'^clientes$', VerClientes, name='Clientes'),
path('orden/<int:id>' ,RealizarOrden, name='Orden'),
url(r'^orden_realizadas$', VerOrdenes, name='Realizadas'),
]