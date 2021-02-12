"""aprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings #para acceder a variables de setting(en este caso para la carga de imagen)

#importat app con mis vistas
from miapp import views
#import piapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/', views.hola_mundo, name="hola_mudo"),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"), #se pueden reusar vistas
    path('pagina-prueba/', views.pagina, name="pagina"),
    path('pagina-prueba/<int:redirigir>/', views.pagina, name="pagina"),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/<str:nombre>/', views.contacto, name='contacto'), #necesaria para el paramtro pcional
    path('contacto/<str:nombre>/<str:apellido>/', views.contacto, name='contacto'),  #necesaria para el paramtro pcional
    #path('crear-articulo/', views.crear_articulo, name='crear-articulo'),
    path('crear-articulo/<str:titulo>/<str:contenido>/<str:publico>/', views.crear_articulo, name='crear-articulo'),
    path('articulo/', views.articulo, name='articlo'),
    path('editar-articulo/<int:id>/', views.editar_articulo, name='editar-articulo'),
    path('articulos/', views.articulos, name='articulos'),
    path("borrar-articulo/<int:id>/", views.borrar_articulo, name='borrar'),
    path('save-article/', views.save_articulo, name='save'),
    path('create-article/', views.create_article, name='create'),
    path('create_full_article/', views.create_full_article, name='create_full')
]


#Configuracion paa cargar imagenes (carpeta media)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)