from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User #importar el modelo User que trae jango para poder captura el id de usuario en el articulo

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categoría'

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default="null", verbose_name="Imagen", upload_to="articles")
    public = models.BooleanField(verbose_name="¿Públicado?")
    user = models.ForeignKey(User, editable=False ,verbose_name="Usuario", on_delete=models.CASCADE) # si le quito editable=False tengo que seleccionar manualmente (una lista select option) el usuario, nota cuando se vaya a usar cualquier propiedad de la tabla user se debe usar el nombre que se le dio en este modelo mas la propiedad en la tabla ejemplo: user.email
    categories= models.ManyToManyField(Category, verbose_name="Categorías", blank=True, related_name="articles") # ManyToManyField crea tabla pivote (tabla referencial o dinamica, es decir relacion muchos a muchos). NOTA: con el related_name="articles" sustituimos usar el *article_set* en las relaciones a la inversa por *articles*
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="actualizado")

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title