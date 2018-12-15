from django.db import models
import datetime 
from apps.Usuario.models import User
from django.utils import timezone
# Create your models here.

class RealizaOrden(models.Model):
	nombre = models.CharField(max_length = 50)
	fecha = models.DateField(("Date"), default=datetime.date.today)
	horainicio = models.TimeField(default=datetime.time(hour=15))
	horafin = models.TimeField()
	modeloascensor = models.CharField(max_length = 50)
	fallasdetectadas = models.CharField(max_length = 200)
	reparacionesefectuadas = models.CharField(max_length = 200)
	cambiopiezas = models.CharField(max_length=200,blank=True,null=True)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE)