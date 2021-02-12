from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at',)
    search_fields = ('name', 'description',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at') #colocamos user solo lectura para saber a quienn le pertenece el ariculo ya que esta editable=False
    search_fields = ('title', 'content', 'user__username', 'categories__name') # el __ es para hacer uso  de la relacion co el modelo para buscar por ese valor en este casos usuario y categoias
    list_display =  ('title', 'user', 'public', 'created_at',)
    list_filter = ('public', 'user__username', 'categories__name')


    def save_model(self, request, obj, form, change): #este metodo es necesario cuando colocamos en el modelo editable=False en usuario de esta manera se guarda el usuario autenticado
        if not obj.user_id:
            obj.user_id = request.user.id
            obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)