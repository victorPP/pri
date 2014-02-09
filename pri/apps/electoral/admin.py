from django.contrib import admin
from pri.apps.electoral.models  import lista_nominal, municipio, enlace_electoral, juridico_municipal, ruta, r_g, juridico_ruta, casilla, r_c, observador_ciudadano, juridico_casilla, casa_amiga

class municipioAdmin(admin.ModelAdmin):
		search_fields = ['nombre']

class lista_nominalAdmin(admin.ModelAdmin):
		list_display = ('nombre','apellido_paterno','apellido_materno','municipio','seccional')
		list_filter = ('municipio','seccional')
		search_fields = ['nombre','apellido_paterno','apellido_materno']

class enlace_electoralAdmin(admin.ModelAdmin):
		list_display = ('nombre','apellido_paterno','apellido_materno','foto_persona','id_municipio','municipio_enlace','seccional')
		list_filter = ('municipio_enlace','seccional')
		search_fields = ['nombre','apellido_paterno','apellido_materno']

class juridico_municipalAdmin(admin.ModelAdmin):
		list_display = ('nombre','apellido_paterno','apellido_materno','id_municipio','municipio_juridico_mun','seccional')
		list_filter = ('municipio_juridico_mun','seccional')
		search_fields = ['nombre','apellido_paterno','apellido_materno']

# -------------------------------- ruta ----------------------------

class rutaAdmin(admin.ModelAdmin):
		list_display = ('numero', 'municipio_ruta','mapa')
		search_fields = ['numero']

class r_g_Admin(admin.ModelAdmin):
		list_display = ('nombre','apellido_paterno','apellido_materno','id_municipio','id_ruta', 'cargo','municipio_r_g','seccional')
		list_filter = ('municipio_r_g','seccional', 'cargo')
		search_fields = ['nombre','apellido_paterno','apellido_materno']

class juridico_rutaAdmin(admin.ModelAdmin):
		list_display = ('id_ruta','nombre','apellido_paterno','apellido_materno','id_municipio','municipio_juridico_ruta','seccional')
		list_filter = ('municipio_juridico_ruta','seccional')
		search_fields = ['nombre','apellido_paterno','apellido_materno']
# ------------------------------- casilla ----------------------------

class casillaAdmin(admin.ModelAdmin):
		list_display = ('numero','id_municipio','id_ruta','seccional','colonia')
		list_filter = ('seccional','colonia')
		search_fields = ['nombre','apellido_paterno','apellido_materno']

class r_cAdmin(admin.ModelAdmin):
		list_display = ('nombre','apellido_paterno','apellido_materno','id_municipio','id_ruta', 'id_casilla','cargo','municipio_r_c','seccional')
		list_filter = ('municipio_r_c','seccional', 'cargo')
		search_fields = ['nombre','apellido_paterno','apellido_materno']

class oc_Admin(admin.ModelAdmin):
		list_display = ('nombre','apellido_paterno','apellido_materno','id_municipio','id_ruta', 'id_casilla','municipio_oc','seccional')
		list_filter = ('municipio_oc','seccional')
		search_fields = ['nombre','apellido_paterno','apellido_materno']

class juridico_casillaAdmin(admin.ModelAdmin):
		list_display = ('nombre','apellido_paterno','apellido_materno','id_municipio','id_ruta', 'id_casilla','municipio_juridico_casilla','seccional')
		list_filter = ('municipio_juridico_casilla','seccional')
		search_fields = ['nombre','apellido_paterno','apellido_materno']

class juridico_casillaAdmin(admin.ModelAdmin):
		list_display = ('nombre','apellido_paterno','apellido_materno','id_municipio','id_ruta', 'id_casilla','municipio_juridico_casilla','seccional')
		list_filter = ('municipio_juridico_casilla','seccional')
		search_fields = ['nombre','apellido_paterno','apellido_materno']

class casa_amigaAdmin(admin.ModelAdmin):
		list_display = ('nombre_propietario','apellido_paterno_propietario','apellido_materno_propietario','municipio_casa_amiga','ruta_casa_amiga', 'casilla_casa_amiga')
		search_fields = ['nombre_propietario']


admin.site.register(lista_nominal, lista_nominalAdmin)
admin.site.register(municipio, municipioAdmin)
admin.site.register(enlace_electoral, enlace_electoralAdmin)
admin.site.register(juridico_municipal, juridico_municipalAdmin)
admin.site.register(ruta,rutaAdmin)
admin.site.register(r_g, r_g_Admin)
admin.site.register(juridico_ruta, juridico_rutaAdmin)
admin.site.register(casilla, casillaAdmin)
admin.site.register(r_c, r_cAdmin)
admin.site.register(observador_ciudadano, oc_Admin)
admin.site.register(juridico_casilla, juridico_casillaAdmin)
admin.site.register(casa_amiga, casa_amigaAdmin)