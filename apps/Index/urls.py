from django.conf.urls import url, include
from apps.Index.views import index, RegistroUsuario,Cliente_List,formulario_view,EditarCliente,EliminarCliente,Cliente_List2,AsignarTecnicoU

from django.urls import include, path

app_name = "index";

urlpatterns = [
url(r'^$', index,name='Menu'),
url(r'^registrar$', RegistroUsuario.as_view()),
url(r'^clientes$', Cliente_List, name='Clientes'),
url(r'^nuevo$', formulario_view, name='Crear_Cliente'),
path('editarCliente/<int:id>' ,EditarCliente, name='EditarCliente'),
path('eliminarCliente/<int:id>' ,EliminarCliente, name='EliminarCliente'),
url(r'^asignaciones$', Cliente_List2, name='Asignaciones'),
path('asignar/<int:id>' ,AsignarTecnicoU, name='AsignarTecnico'),
]