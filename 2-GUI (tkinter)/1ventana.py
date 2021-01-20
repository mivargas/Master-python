"""
#tkinter 
modulo para crear interfaces graficas de usuario
"""
from tkinter import *
import pathlib #ruta absoluta

#crear la ventana raiz

ventana = Tk()

#icono de la ventana (favicon)
ruta_icono = str(pathlib.Path().absolute())  + "/imagenes/labsxd.png"
#ventana.iconbitmap(ruta) #no funciona en linux, en todo caso usar el metodo de abajo
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