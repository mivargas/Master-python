"""
#tkinter 
modulo para crear interfaces graficas de usuario
"""
from tkinter import *
import os.path #ruta absoluta

class Programa:
    def __init__(self):
        self.title = "Master en ppython"
        self.icon = './imagenes/labsxd.png'
        self.icon_alt = './2-GUI (tkinter)/imagenes/labsxd.png'
        self.size = "770x470"
        self.resizable = False

    def cargar(self):
        #crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #comprobar si existe ruta 
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)


        #mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        #icono de la ventana (favicon)
        img = PhotoImage(file=ruta_icono)
        ventana.tk.call('wm', 'iconphoto', ventana._w, img)

        #titulo de la ventana
        ventana.title(self.title)

        #cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        #bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0) #cero inactivo 1 es activo, es decir si fuera (1,0) puedo redimensionar el ancho mas no el alto

    def addtexto(self, dato):
        #texto = Label(self.ventana, text= "hola desde un metodo")
        texto = Label(self.ventana, text= dato)
        texto.pack()
    
    def mostrar(self):
        self.ventana.mainloop()

programa = Programa()
programa.cargar()
#programa.addtexto()
programa.addtexto("hola")
programa.addtexto("todo el mundo")
programa.addtexto("es cool")
programa.mostrar()

