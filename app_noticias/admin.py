from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista principal
    list_display = ('titulo', 'fecha', 'lugar', 'fecha_creacion')

    # Filtros laterales para filtrar rapidamente por fecha o lugar
    list_filter = ('fecha', 'lugar')

    # Barra de busqueda en la parte superior
    search_fields = ('titulo', 'descripcion', 'lugar')

    # Navegacion por fechas en la parte superior
    date_hierarchy = 'fecha'

    # Permite editar el campo 'lugar' directamente desde la lista
    # sin necesidad de entrar a la noticia

# Personalizacion global del Admin (Titulos institucionales)
admin.site.site_header = "Administracion Portal de Noticias SENA"
admin.site.site_title = "Portal de Noticias SENA"
admin.site.index_title = "Centro de Automatizacion Industrial - Regional Valle"

