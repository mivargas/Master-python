from django.db import models

#pip3 install pylint-django // se recomienda instalar este paquete para un mejor reconocimiento de las clases de Django y en los ajustes de VSC en extetensiones python buscar pylint cambiaro por pylint_django

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10, verbose_name="Título") #con verbose_name definimos con que nombre quermos que se muestre en el panel de administracion, de no colocarlos se usara el nombre del campo en la tabla por defecto
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Miniatura", upload_to="articles") #el ultimo parametro es la sub carpeta que se creara al subir la imagen
    public = models.BooleanField(verbose_name="¿Públicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Editado")

    class Meta:
        #db_table = "" #forzar un nombre de tabla
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos" 
        ordering = ['-created_at'] #ordenar por id ascendente, si lo quisiera descendente seria '-id'

    def __str__(self): #metodo magico para mostrar un sring a nuestro gusto en vez de object(1) en la lista del panel admin
        if self.public == True:
            publico = "(públicado)"
        else:
            publico = "(privado)"
        return f"{self.title} {publico}"
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    