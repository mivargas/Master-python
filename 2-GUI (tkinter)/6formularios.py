from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("formularios")

#texto encabezado

encabezado=Label(ventana, text="formalario con tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Snas", 18),
    padx=10,
    pady=10
)
#encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=2, stick=W)

#label para el campo (nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

#campo de texto (nombre)
campo_texto=Entry(ventana)
campo_texto.config(state="normal", justify="right")
campo_texto.grid(row=1, column=1, padx=5, pady=5, sticky=W)


#label para el campo (apellido)
label = Label(ventana, text="Apellido")
label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

#campo de texto (apellido)
campo_texto=Entry(ventana)
campo_texto.config(state="disabled", justify="left")
campo_texto.grid(row=2, column=1, padx=5, pady=5, sticky=W)


#label para el campo (descripcion )
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, padx=5, pady=5, sticky=N)

#campo de texto GRANDE
campo_grande = Text(ventana)
campo_grande.config(
    width=30, 
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
)
campo_grande.grid(row=3, column=1)

Label(ventana).grid(row=4, column=1)

#boton
boton= Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=15, pady=15, bg="green", fg="white")


ventana.mainloop()