from django.contrib import admin
from .models import Page

#configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at', 'updated_at',) 
    search_fields = ('title', 'content',) #configurar filtro de usqueda
    list_filter = ('visible',) #menu filtro lateral
    list_display = ('title', 'visible', 'created_at',)  #personalizar lista (cabecera de tabla)
    ordering = ('created_at',) #orden de los registros

# Register your models here.
admin.site.register(Page, PageAdmin)


#Configuracion del panel
title="Proyecto con Django"
subtitulo="Panel de Gestión"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitulo