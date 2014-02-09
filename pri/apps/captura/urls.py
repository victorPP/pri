from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('pri.apps.captura.views',
		url(r'^captura/','captura_view', name='inicio_captura'),
		url(r'^captura/municipio','captura_view', name='inicio_captura'),
)