from django.db import models

class Egresado(models.Model):

	estado = (
    ('Graduado', 'Graduado'),
    ('Pendiente', 'Pendiente'),
	)
	estado_egresado = models.CharField(max_length=10,choices = estado)
	nombre_egresado = models.CharField (max_length=100)
	apellido_egresado = models.CharField (max_length=100)
	dir_egresado = models.CharField (max_length=100)
	tel_egresado = models.CharField (max_length=100)
	titulo_egresado = models.CharField (max_length=100)
	email_egresado = models.EmailField (max_length = 75)
	fecha_fin = models.DateTimeField (auto_now_add=False)
	id_egresado = models.CharField (max_length=100)
	
	def __str__(self):
		return str("%s %s" %(self.nombre_egresado,self.titulo_egresado[:60]))

class Postgrado(models.Model):

	titulo_postgrado = models.CharField(max_length=100)
	ano_inicio = models.DateTimeField(auto_now_add=False)
	ano_fin = models.DateTimeField(auto_now_add=False)
	identrad = models.ForeignKey(Egresado)

	def __str__(self):
		return self.titulo_postgrado

class Experiencia(models.Model):

	cargo = models.CharField(max_length=100)
	fecha_inicio = models.DateTimeField(auto_now_add=False)
	fecha_fin = models.DateTimeField(auto_now_add=False)
	empresa = models.CharField(max_length=100)
	identra = models.ForeignKey(Egresado)

	def __str__(self):
		return self.empresa


class Red(models.Model):

	nombre_red = models.CharField(max_length=100)
	fecha_inicio = models.DateTimeField(auto_now_add=False)
	nombre_director = models.CharField(max_length=100)
	email_contacto = models.EmailField (max_length = 75)
	identr = models.ForeignKey(Egresado)

	def __str__(self):
		return self.nombre_red