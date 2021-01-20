from tkinter import *

ventana =  Tk()

ventana.geometry("700x700")
ventana.config(
    bd=50,
    bg="#ccc"
)

def getDato():
    resultado.set(dato.get())
    if len(resultado.get()) >=1:
        dato_recogido.config(
        bg="green",
        fg="white"
    )
        

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Mete un texto:").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="dato recogido:").pack(anchor=NW)
dato_recogido = Label(ventana, textvariable=resultado)
dato_recogido.pack(anchor=NW)

Button(ventana, text="mostrar dato", command=getDato).pack(anchor=NW)
ventana.mainloop()