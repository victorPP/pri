from django.shortcuts import render_to_response
from django.template import RequestContext
from pri.apps.electoral.models  import lista_nominal, municipio, enlace_electoral, juridico_municipal, ruta, r_g, juridico_ruta, casilla, r_c, observador_ciudadano, juridico_casilla, casa_amiga

from  django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

def captura_view(request):
		mun = municipio.objects.filter()
		ctx = {'municipio':mun}
		return render_to_response('captura/principal.html', ctx , context_instance=RequestContext(request))

def captura_municipio(request):
			if request.method == "POST":
					municipio_id = POST['municipio']
					mun = municipio.objects.filter(id=municipio_id)
					rut = ruta.objects.filter(municipio_ruta=municipio_id)
					ctx = {'municipio':mun,'ruta':rut}
					return render_to_response('captura/municipio.html', ctx ,context_instance=RequestContext(request))
			else:
					return HttpResponseRedirect('/captura/')
