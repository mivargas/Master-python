from tkinter import *
from tkinter import messagebox as mensaje

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    #mensaje.showinfo("Alerta", "Hola soy miguel")
    #mensaje.showwarning("Alerta", "Hola soy miguel")
    mensaje.showerror("Alerta", "Hola soy miguel")

Button(ventana, text="Mostrar ventana", command=sacarAlerta).pack()


def salir(nombre):
    #mensaje.showinfo("Alerta", "Hola soy miguel")
    #mensaje.showwarning("Alerta", "Hola soy miguel")
    resultado = mensaje.askquestion("Salir", "¿Quieres continuar ejecutando la applicacion?")

    if resultado != "yes":
        mensaje.showinfo("Chao!!", f"Adios {nombre}" )
        ventana.destroy()

#Button(ventana, text="Salir", command=salir).pack()
Button(ventana, text="Salir", command= lambda: salir("Miguel")).pack() #solo colocar lambda cuando hay parametros de funcion


ventana.mainloop()