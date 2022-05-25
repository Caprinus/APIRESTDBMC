from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
# Create your models here.

class Post(TimeStampedModel, SoftDeletableModel):
	title 				= models.CharField(max_length=50, null=False, blank=True)
	body 				= models.TextField(max_length=5000, null=False, blank=True)
	date_published 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
	slug 				= models.SlugField(blank=True, unique=True)
	def __str__(self):
		return self.title


class Casa(models.Model):
    id_condominio = models.IntegerField(max_length=8) 
    descripcion = models.CharField(max_length=200)
    saldo = models.IntegerField(max_length=8) 
    luz = models.IntegerField(max_length=8) 
    agua = models.IntegerField(max_length=8) 

class Condominio(models.Model):
    nombre_condominio = models.CharField(max_length=200)
    num_casas = models.IntegerField(max_length=8) 
    num_casas_ocupadas = models.IntegerField(max_length=8) 
    mantencion = models.IntegerField(max_length=8) 


class Espacios_comunes(models.Model):
    id_condominio = models.IntegerField(max_length=8) 
    tipo_espacio = models.CharField(max_length=50)
    costo_arriendo = models.IntegerField(max_length=8) 
    mantencion = models.IntegerField(max_length=8) 
    aforo = models.IntegerField(max_length=8) 
    ocupado = models.CharField(max_length=2)
    
class Usuario(models.Model):      
    rut = models.CharField(max_length=10) 
    nombres = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=10)
    casa = models.IntegerField(max_length=8) 
    condominio = models.IntegerField(max_length=8) 
    directiva = models.CharField(max_length=2)
    conserje = models.CharField(max_length=2)
    horario = models.CharField(max_length=100)
    fecha_ingreso = models.CharField(max_length=50)
    habilitado = models.IntegerField(max_length=2)
 
class Seguridad(models.Model):
    correo_usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)
    habilitado = models.IntegerField(max_length=2)

