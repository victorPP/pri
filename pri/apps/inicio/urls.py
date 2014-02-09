from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('pri.apps.inicio.views',
		url(r'^$','index_view', name='vista_inicio'),
)