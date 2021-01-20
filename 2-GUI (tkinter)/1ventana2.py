"""
#tkinter 
modulo para crear interfaces graficas de usuario
"""
from tkinter import *
import os.path #ruta absoluta

#crear la ventana raiz

ventana = Tk()

#comprobar si existe ruta 
ruta_icono = os.path.abspath('./imagenes/labsxd.png')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./2-GUI (tkinter)/imagenes/labsxd.png')


#mostrar texto en el programa
texto = Label(ventana, text=ruta_icono)
texto.pack()

#icono de la ventana (favicon)
img = PhotoImage(file=ruta_icono)
ventana.tk.call('wm', 'iconphoto', ventana._w, img)

#titulo de la ventana
ventana.title("Interface grafica")

#cambio en el tamaño de la ventana
ventana.geometry("750x450")

#bloquear el tamaño de la ventana
ventana.resizable(0,0) #cero inactivo 1 es activo, es decir si fuera (1,0) puedo redimensionar el ancho mas no el alto


#arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()