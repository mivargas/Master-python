from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required #necesario el modulo para el decorador de restriccion de accso a algunas vistas al momento de estar logueado

# Create your views here.

@login_required(login_url="login") #decorador de python le indica al metodo que para entrar en esa vista debe estar logueado (se uso antes del metodo def) redirecciona al login
def page(request, slug):
    
    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
        "page": page
    }) 