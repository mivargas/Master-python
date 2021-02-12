from django.contrib import admin
from .models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin): #declaro esta clase si quiero quese vean campos de solo lectura como created_at y updated_at, debo pasarlo como segundo parametro al metodo register de abajo
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin) #recibe los campos de solo lectura en el segundo parametro
admin.site.register(Category)


#Configurar el titulo del panel
title_web = "Master en pyhon - Desarrollo Miguel Vargas"
admin.site.site_header = title_web
admin.site.site_title = title_web
admin.site.index_title = "Panel de gestión" #cambiar titulo del inicio (sitio administrativo)