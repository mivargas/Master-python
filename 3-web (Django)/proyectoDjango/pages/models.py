from django.db import models
from ckeditor.fields import RichTextField #erriquecedor d texto se tiene que intalar con pip3 install django-ckeditor

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título")
    #content = models.TextField(verbose_name="Contenido")
    content = RichTextField(verbose_name="Contenido") # se cambia el textarea pof RichTextField (sin models. ya que es un paquete eterno)
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")
    order = models.IntegerField(verbose_name="Orden", default=0)
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Acualizado el")

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.title
        