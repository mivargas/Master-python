from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category #importamos los modelos para oder usar la capa de abstraccion ORM
from django.db.models import Q #necario para las consultas ORM que contenan una condicion OR
from miapp.forms import FormArticle #se necesita para form API
from django.contrib import messages #mensajes flash

# Create your views here.
layout="""

"""
def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050</p>
        <ul>
    ""

    year = 2020
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{year}</li>"
        year +=1

    html+="</ul>"
"""
    year = 2021
    hasta = range(year, 2051)

    nombre = 'Miguel Vargas'

    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
        })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=None):
    if redirigir == 1:
        #return redirect('/inicio/') #se usa la tota norma (no name)
        return redirect('contacto', nombre="miguel", apellido="vargas") #puedo enviar parametros para la ruta a redirigir (NOTA AQUI SE USA EL NOMBRE DE LA RUTA NO LA RUTA COMO TAL ES DECIR 'name')
    return render(request, 'pagina.html', {
        'texto': '',
        'lista': ['uno', 'dos', 'tres']
    })

def contacto(request, nombre="", apellido=""): # es un parametro opcional
    html = ""

    if nombre and apellido:
        html = f"El nombre completo es: <h3>{nombre} {apellido}</h3>"
    #return HttpResponse(layout+f"<h2>Contacto {nombre} {apellido}</h2>")
    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

"""
def crear_articulo(request):
    articulo = Article(
        title = 'primer articulo',
        content = 'Conetenido del articulo',
        public = True
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")
"""

def crear_articulo(request, titulo, contenido, publico):
    articulo = Article(
        title = titulo,
        content = contenido,
        public = publico
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")


def articulo(request):
    #articulo = Article.objects.get(pk=5)
    #articulo = Article.objects.get(id=5)
    #articulo = Article.objects.get(title="notas de prueba en Django")

    try:
        articulo = Article.objects.get(title="notas de prueba en Django", public=True)

        response = (f"Articulo:<br> {articulo.id}. {articulo.title}")
    except:
        response = "NO existe el articulo"
    
    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "batman"
    articulo.content = "pelicula 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo editado: {articulo.id}. {articulo.title} - {articulo.content}")

def articulos(request):
    articulos = Article.objects.all()
    #articulos = Article.objects.order_by('title')
    #articulos = Article.objects.order_by('title')[:3] #un limit muestra oslo 3
    #articulos = Article.objects.order_by('title')[3:3] #mostrar en un rango
    #articulos = Article.objects.order_by('-title') #descendente
    #articulos = Article.objects.filter(title="notas de prueba en Django") # la diferencia de este con get() es que filter devueve multiples registros
    
    """LOOKUPS"""
    #articulos = Article.objects.filter(title__contains="nota")  #funciona como like en sql
    #articulos = Article.objects.filter(title__exact="nota") #esto es nombre exacto (basicamente es igual que decir title="nota")
    #articulos = Article.objects.filter(title__iexact="BatmaN") #no tiene sensibilidad por payusculas y minusculas o haya letras intercaladas
    #articulos = Article.objects.filter(id__gt=4) #gt es MAS GRANDE QUE... es decir muestras solo los id mayores de 4
    #articulos = Article.objects.filter(id__gte=4) #gte es MAS GRANDE QUE O IGUAL QUE...
    #articulos = Article.objects.filter(id__lt=4) #gte es MAS PEQUEÑO QUE...
    #articulos = Article.objects.filter(id__lte=4) #gte es MAS PEQUEÑO QUE O IGUAL QUE...
    #articulos = Article.objects.filter(id__lt=3, title__contains="nota") #convinacion de lookups

    """EXCLUDE"""
    #articulos = Article.objects.filter(title="notas de prueba en Django").exclude(public=False) #se puede hacer lo mismo aladiendo la condicion en filter y asi no usaar el exclude
    
    """Consultas SQL desde Django"""
    #articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title = 'notas de prueba en Django' AND public = True ")

    """OR"""
    #articulos= Article.objects.filter( Q(title__contains="articulo") | Q(title__contains="batman") ) #hacer condicion OR (o)

    return render(request, 'articulos.html', {
        'articulos': articulos
    })


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')


def save_articulo(request):
    """
    if request.method == 'GET':

        titulo = request.GET['title']
        contenido = request.GET['content']
        publico = request.GET['public']
    """
    if request.method == 'POST':

        titulo = request.POST['title']
        contenido = request.POST['content']
        publico = request.POST['public']

        articulo = Article(
            title = titulo,
            content = contenido,
            public = publico
        )
        articulo.save()
        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido guardar el articulo</h2>")

def create_article(request):
    return render(request, 'create_article.html')


def create_full_article(request):
    if request.method == 'POST':

        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            titulo = data_form.get('title')
            contenido = data_form['content']
            publico = data_form.get('public')

            articulo = Article(
            title = titulo,
            content = contenido,
            public = publico
            )

            articulo.save()

            #crear mensaje cflash (sesion que solo se muestra una vez)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            return redirect('articulos')
            #return HttpResponse(articulo.title + ' ' + articulo.content + ' ' + str(articulo.public))
    else:
        formulario = FormArticle()
    
    return render(request, "create_full_article.html", {
        'form':formulario
    })
