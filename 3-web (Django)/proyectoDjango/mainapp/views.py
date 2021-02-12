from django.shortcuts import render, redirect
from django.contrib import messages #importar modulo paa mensajes flash
from django.contrib.auth.forms import UserCreationForm #importar formulario de registro de django
from mainapp.forms import RegisterForm

from django.contrib.auth import authenticate, login, logout #modulo para logueo, autenticacion y cerrar sesion
# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre nosotros'
    })

def register_page(request):
    if request.user.is_authenticated: #si esta autenticado no debe mostrar el registro redirecciona a inicio

        return redirect("inicio")

    else:
        #register_form = UserCreationForm() #instanciar la clase de creacion de formulario por defecto de django
        register_form = RegisterForm() #intanciar formulario prsonalzado (forms.py)

        if request.method == 'POST':
            #register_form = UserCreationForm(request.POST) #si se ha enviado algo se guardara 
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente') #crear mensaje flash

                return redirect('inicio')

        return render(request, 'users/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request): #si esta autenticado no debe mostrar el login redirecciona a inicio
    if request.user.is_authenticated:

        return redirect("inicio")

    else:

        if request.method == 'POST':
            username = request.POST.get('username') #el name de los campos del formulario
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password) #llamamos al objeto authenticate y le pasamos los parametros de user y pass

            if user is not None: #si devuelve algun usuario
                login(request, user) #crea el login con los datos que obtuvo de user
                return redirect('inicio') #redirecciona
            else:
                messages.warning(request, 'No te has identificado correctamente') #crear mensaje flash si no devuelve ningun usuario


        return render(request, 'users/login.html', {
            'title': 'Identificate'
        })

def logout_user(request):
    logout(request) #asi se llama al metodo logout del modulo de contrib de django

    return redirect('login')
