from django.db import models 



class lista_nominal(models.Model):
		municipio = models.CharField(max_length=40)
		seccional = models.CharField(max_length=20)
		clave_elector = models.CharField(max_length=18)
		nombre = models.CharField(max_length=40)
		apellido_paterno = models.CharField(max_length=40)
		apellido_materno = models.CharField(max_length=40)
		calle = models.CharField(max_length=50)
		numero = models.IntegerField(max_length=6)
		colonia = models.CharField(max_length=30)

		def __unicode__(self):
			nombreCompleto = ("%s %s %s") %(self.nombre, self.apellido_paterno, self.apellido_materno)
			return nombreCompleto


# -------------------------------------------------------------- primer padre (municipio)
class municipio(models.Model):
		nombre = models.CharField(max_length=30)


		def __unicode__(self):

			return self.nombre

# --------------------   primer estrato ( municipio)  ------------------------------------
class enlace_electoral(models.Model):

		def url_fotografias(self,filename):
			ruta = "fotografias/%s/%s"%(self.clave_elector,str(filename))
			return ruta
		
		def url_credenciales(self,filename):
			ruta = "credenciales/%s/%s"%(self.clave_elector,str(filename))
			return ruta

		def foto_persona(self):
			return '<img scr="/media/%s" width=50px heigth=50px />' %(self.fotografia)

		foto_persona.allow_tags = True

		municipio_enlace = models.CharField(max_length=40)
		seccional = models.CharField(max_length=20)
		clave_elector = models.CharField(max_length=18)
		nombre = models.CharField(max_length=40)
		apellido_paterno = models.CharField(max_length=40)
		apellido_materno = models.CharField(max_length=40)
		calle = models.CharField(max_length=50)
		numero = models.IntegerField(max_length=6)
		colonia = models.CharField(max_length=30)
		telefono = models.IntegerField(max_length=10)
		fotografia = models.ImageField(upload_to=url_fotografias)
		credencial_elector = models.ImageField(upload_to=url_credenciales)
		reconocimiento = models.BooleanField()
		nombramiento = models.BooleanField()
		credencial = models.BooleanField()
		usuario_captura = models.CharField(max_length=20)
		id_municipio = models.ForeignKey(municipio)

		def __unicode__(self):
			nombreCompleto = ("%s %s %s") %(self.nombre, self.apellido_paterno, self.apellido_materno)
			return nombreCompleto


class juridico_municipal(models.Model):

		def url_fotografias(self,filename):
			ruta = "fotografias/%s/%s"%(self.clave_elector,str(filename))
			return ruta
		
		def url_credenciales(self,filename):
			ruta = "credenciales/%s/%s"%(self.clave_elector,str(filename))
			return ruta

			
		municipio_juridico_mun = models.CharField(max_length=40)
		seccional = models.CharField(max_length=20)
		clave_elector = models.CharField(max_length=18)
		nombre = models.CharField(max_length=40)
		apellido_paterno = models.CharField(max_length=40)
		apellido_materno = models.CharField(max_length=40)
		calle = models.CharField(max_length=50)
		numero = models.IntegerField(max_length=6)
		colonia = models.CharField(max_length=30)
		telefono = models.IntegerField(max_length=10)
		fotografia = models.ImageField(upload_to=url_fotografias)
		credencial_elector = models.ImageField(upload_to=url_credenciales)
		reconocimiento = models.BooleanField()
		nombramiento = models.BooleanField()
		credencial = models.BooleanField()
		usuario_captura = models.CharField(max_length=20)
		id_municipio = models.ForeignKey(municipio)

		def __unicode__(self):
			nombreCompleto = ("%s %s %s") %(self.nombre, self.apellido_paterno, self.apellido_materno)
			return nombreCompleto

# --------------------  fin del primer estrato (municipio)  ------------------------------------


# -------------------------------------------------------------- segundo padre (ruta)--->(municipio)
class ruta(models.Model):
		numero = models.CharField(max_length=10)
		mapa = models.FileField(upload_to='mapas/rutas')
		municipio_ruta = models.ForeignKey(municipio)

		def __unicode__(self):
				return self.numero


# --------------------   segundo estrato (ruta)--->(municipio)  ------------------------------------

class r_g(models.Model):

		def url_fotografias(self,filename):
			ruta = "fotografias/%s/%s"%(self.clave_elector,str(filename))
			return ruta
		
		def url_credenciales(self,filename):
			ruta = "credenciales/%s/%s"%(self.clave_elector,str(filename))
			return ruta


		CARGO = (
			('Representante General Propietario', 'rg_propietario'),
		    ('Representante General Suplente', 'rg_suplente'),
	    )

		municipio_r_g = models.CharField(max_length=40)
		seccional = models.CharField(max_length=20)
		clave_elector = models.CharField(max_length=18)
		cargo = models.CharField(max_length=50,choices=CARGO )
		nombre = models.CharField(max_length=40)
		apellido_paterno = models.CharField(max_length=40)
		apellido_materno = models.CharField(max_length=40)
		calle = models.CharField(max_length=50)
		numero = models.IntegerField(max_length=6)
		colonia = models.CharField(max_length=30)
		telefono = models.IntegerField(max_length=10)
		fotografia = models.ImageField(upload_to=url_fotografias)
		credencial_elector = models.ImageField(upload_to=url_credenciales)
		reconocimiento = models.BooleanField()
		nombramiento = models.BooleanField()
		credencial = models.BooleanField()
		usuario_captura = models.CharField(max_length=20)
		id_ruta = models.ForeignKey(ruta)
		id_municipio = models.ForeignKey(municipio)

		def __unicode__(self):
			nombreCompleto = ("%s %s %s") %(self.nombre, self.apellido_paterno, self.apellido_materno)
			return nombreCompleto

			
class juridico_ruta(models.Model):

		def url_fotografias(self,filename):
			ruta = "fotografias/%s/%s"%(self.clave_elector,str(filename))
			return ruta
		
		def url_credenciales(self,filename):
			ruta = "credenciales/%s/%s"%(self.clave_elector,str(filename))
			return ruta

		municipio_juridico_ruta = models.CharField(max_length=40)
		seccional = models.CharField(max_length=20)
		clave_elector = models.CharField(max_length=18)
		nombre = models.CharField(max_length=40)
		apellido_paterno = models.CharField(max_length=40)
		apellido_materno = models.CharField(max_length=40)
		calle = models.CharField(max_length=50)
		numero = models.IntegerField(max_length=6)
		colonia = models.CharField(max_length=30)
		telefono = models.IntegerField(max_length=10)
		fotografia = models.ImageField(upload_to=url_fotografias)
		credencial_elector = models.ImageField(upload_to=url_credenciales)
		reconocimiento = models.BooleanField()
		nombramiento = models.BooleanField()
		credencial = models.BooleanField()
		usuario_captura = models.CharField(max_length=20)
		id_ruta = models.ForeignKey(ruta)
		id_municipio = models.ForeignKey(municipio)

		def __unicode__(self):
			nombreCompleto = ("%s %s %s") %(self.nombre, self.apellido_paterno, self.apellido_materno)
			return nombreCompleto

# --------------------  fin del segundo estrato (ruta)--->(municipio)  ------------------------------------



# -------------------------------------------------------------- tercer padre (casilla)--->(ruta)--->(municipio)
class casilla(models.Model):
		numero = models.CharField(max_length=20)
		seccional = models.CharField(max_length=30)
		calle = models.CharField(max_length=40)
		numero = models.CharField(max_length=6)
		colonia = models.CharField(max_length=30)
		observaciones = models.TextField()
		fotografia = models.ImageField(upload_to='fotografias/casillas')
		mapa = models.FileField(upload_to='mapas/casillas')
		id_ruta = models.ForeignKey(ruta)
		id_municipio = models.ForeignKey(municipio)

		def __unicode__(self):
				return self.numero

# --------------------   tercer estrato (casilla)--->(ruta)--->(municipio)  ------------------------------------

class r_c(models.Model):

		def url_fotografias(self,filename):
			ruta = "fotografias/%s/%s"%(self.clave_elector,str(filename))
			return ruta
		
		def url_credenciales(self,filename):
			ruta = "credenciales/%s/%s"%(self.clave_elector,str(filename))
			return ruta


		CARGO= (
	        ('Representante Casilla Propietario 1', 'rc_propietario1'),
	        ('Representante Casilla Propietario 2 ', 'rc_propietario2'),
	        ('Representante Casilla Suplente', 'rc_suplente'),
	    )

		municipio_r_c = models.CharField(max_length=40)
		seccional = models.CharField(max_length=20)
		clave_elector = models.CharField(max_length=18)
		cargo = models.CharField(max_length=50,choices=CARGO )
		nombre = models.CharField(max_length=40)
		apellido_paterno = models.CharField(max_length=40)
		apellido_materno = models.CharField(max_length=40)
		calle = models.CharField(max_length=50)
		numero = models.IntegerField(max_length=6)
		colonia = models.CharField(max_length=30)
		telefono = models.IntegerField(max_length=10)
		fotografia = models.ImageField(upload_to=url_fotografias)
		credencial_elector = models.ImageField(upload_to=url_credenciales)
		reconocimiento = models.BooleanField()
		nombramiento = models.BooleanField()
		credencial = models.BooleanField()
		usuario_captura = models.CharField(max_length=20)
		id_casilla = models.ForeignKey(casilla)
		id_ruta = models.ForeignKey(ruta)
		id_municipio = models.ForeignKey(municipio)

		def __unicode__(self):
			nombreCompleto = ("%s %s %s") %(self.nombre, self.apellido_paterno, self.apellido_materno)
			return nombreCompleto

class observador_ciudadano(models.Model):

		def url_fotografias(self,filename):
			ruta = "fotografias/%s/%s"%(self.clave_elector,str(filename))
			return ruta
		
		def url_credenciales(self,filename):
			ruta = "credenciales/%s/%s"%(self.clave_elector,str(filename))
			return ruta


		municipio_oc = models.CharField(max_length=40)
		seccional = models.CharField(max_length=20)
		clave_elector = models.CharField(max_length=18)
		nombre = models.CharField(max_length=40)
		apellido_paterno = models.CharField(max_length=40)
		apellido_materno = models.CharField(max_length=40)
		calle = models.CharField(max_length=50)
		numero = models.IntegerField(max_length=6)
		colonia = models.CharField(max_length=30)
		telefono = models.IntegerField(max_length=10)
		fotografia = models.ImageField(upload_to=url_fotografias)
		credencial_elector = models.ImageField(upload_to=url_credenciales)
		reconocimiento = models.BooleanField()
		nombramiento = models.BooleanField()
		credencial = models.BooleanField()
		usuario_captura = models.CharField(max_length=20)
		id_casilla = models.ForeignKey(casilla)
		id_ruta = models.ForeignKey(ruta)
		id_municipio = models.ForeignKey(municipio)

		def __unicode__(self):
			nombreCompleto = ("%s %s %s") %(self.nombre, self.apellido_paterno, self.apellido_materno)
			return nombreCompleto


class juridico_casilla(models.Model):

		def url_fotografias(self,filename):
			ruta = "fotografias/%s/%s"%(self.clave_elector,str(filename))
			return ruta
		
		def url_credenciales(self,filename):
			ruta = "credenciales/%s/%s"%(self.clave_elector,str(filename))
			return ruta


		municipio_juridico_casilla = models.CharField(max_length=40)
		seccional = models.CharField(max_length=20)
		clave_elector = models.CharField(max_length=18)
		nombre = models.CharField(max_length=40)
		apellido_paterno = models.CharField(max_length=40)
		apellido_materno = models.CharField(max_length=40)
		calle = models.CharField(max_length=50)
		numero = models.IntegerField(max_length=6)
		colonia = models.CharField(max_length=30)
		telefono = models.IntegerField(max_length=10)
		fotografia = models.ImageField(upload_to=url_fotografias)
		credencial_elector = models.ImageField(upload_to=url_credenciales)
		reconocimiento = models.BooleanField()
		nombramiento = models.BooleanField()
		credencial = models.BooleanField()
		usuario_captura = models.CharField(max_length=20)
		id_casilla = models.ForeignKey(casilla)
		id_ruta = models.ForeignKey(ruta)
		id_municipio = models.ForeignKey(municipio)

		def __unicode__(self):
			nombreCompleto = ("%s %s %s") %(self.nombre, self.apellido_paterno, self.apellido_materno)
			return nombreCompleto


class casa_amiga(models.Model):
		nombre_propietario = models.CharField(max_length=80)
		apellido_paterno_propietario = models.CharField(max_length=80)
		apellido_materno_propietario = models.CharField(max_length=80)
		foto = models.ImageField(upload_to='fotos/casas_amigas')
		mapa = models.FileField(upload_to='mapas/casas_amigas')
		casilla_casa_amiga = models.ForeignKey(casilla)
		municipio_casa_amiga = models.ForeignKey(municipio)
		ruta_casa_amiga = models.ForeignKey(ruta)

		def __unicode__(self):
				NombreCasa = ("%s %s %s") %(self.nombre_propietario, self.apellido_paterno_propietario, self.apellido_materno_propietario)
				return NombreCasa

# --------------------  fin del tercer estrato (casilla)--->(ruta)--->(municipio)  ------------------------------------

