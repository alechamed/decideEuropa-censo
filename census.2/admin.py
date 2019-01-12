from django.contrib import admin
#Estos he añadido
from .resources import CensusResources
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
#Hasta aqui
from .models import Census

#class CensusAdmin(admin.ModelAdmin):
#    list_display = ('voting_id', 'voter_id')
#    list_filter = ('voting_id', )
#
#    search_fields = ('voter_id', )

#Metodo para exportar
def export_selected(modeladmin, request, queryset):
	#LLamo a censusResource para exportarlo despues
	census_resource = CensusResources()
	#Exporto los censos seleccionados
	dataset = census_resource.export(queryset)
	#Creo una respuesta http con los censos en excel
	response = HttpResponse (dataset.xls, content_type='text/xls')
	#Pongo a disposicion el excel con el nombre census.xls
	response['Content-Disposition'] = 'attachment; filename="census.xls"'
	#Devuelvo la respuesta del metodo
	return response
#Le pongo un nombre para que salga en la lista de acciones
export_selected.short_description = 'Export selected as xls'

#Cambié la entrada del census admin para añadir el boton import/export
class CensusAdmin(ImportExportModelAdmin):
	#Se añade esta linea para añadir los botones import/export
	resource_class = CensusResources
	list_display = ('voting_id', 'voter_id')
	list_filter = ('voting_id', )

	search_fields = ('voter_id', )
	#Se añade el metodo de export a la lista de acciones de django
	actions = [export_selected, ]

admin.site.register(Census, CensusAdmin)
