from django.db import models
from django.contrib.auth.models import User

class AmpliacionPerfil(models.Model):
		PERMISOS = (
			('capturista', 'capturista'),
		    ('editor', 'editor'),
		    ('consultor', 'consultor'),
		    ('enlace', 'enlace'),
	    )

		user = models.OneToOneField(User)
		permiso = models.CharField(max_length=20,choices=PERMISOS)
		telefono = models.CharField(max_length=20)

		def __unicode__(self):
				return self.user.username
