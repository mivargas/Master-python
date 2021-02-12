from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout="""
<h1>Sitio Web con django | Miguel Vargas</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-prueba">Página de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>

</ul>
<hr/>
"""
def index(request):
    
    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050</p>
        <ul>
    """

    year = 2020
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{year}</li>"
        year +=1

    html+="</ul>"
    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse(layout+"""
        <h1>HOLA MUNDO CON DJANGO!!!!</h1>
        <h3>Soy Miguel</h3>
    """)
    
def pagina(request, redirigir=None):
    if redirigir == 1:
        #return redirect('/inicio/') #se usa la tota norma (no name)
        return redirect('contacto', nombre="miguel", apellido="vargas") #puedo enviar parametros para la ruta a redirigir (NOTA AQUI SE USA EL NOMBRE DE LA RUTA NO LA RUTA COMO TAL ES DECIR 'name')
    return HttpResponse(layout+"""
        <h1>Página de mi web</h1>
        <p>Creado por Miguel</p>
    """)

def contacto(request, nombre="", apellido=""): # es un parametro opcional
    html = ""

    if nombre and apellido:
        html = f"El nombre completo es: <h3>{nombre} {apellido}</h3>"
    #return HttpResponse(layout+f"<h2>Contacto {nombre} {apellido}</h2>")
    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)