from django.db import models
from apps.Usuario.models import User

# Create your models here.



class Cliente(models.Model):
	nombre = models.CharField(max_length = 50)
	direccion = models.TextField(max_length=50)
	ciudad = models.TextField(max_length=50)
	comuna = models.TextField(max_length=50)
	telefono = models.CharField(max_length=8)
	correo = models.EmailField(unique=True)



class AsignarTecnicos(models.Model):
	nombre = models.CharField(max_length = 50)
	direccion = models.TextField(max_length=50)
	ciudad = models.TextField(max_length=50)
	comuna = models.TextField(max_length=50)
	telefono = models.CharField(max_length=8)
	correo = models.EmailField()
	id_cliente = models.CharField(max_length=500)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE)


