from tkinter import *

ventana = Tk()

ventana.title("Marcos | Master en python")
ventana.geometry("700x700")


marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue"
)
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES) #el anchor es para que se apegue lo mas posible al borde superor, np basta el top es igual en el caso del de abajo seria N con bottom

marco = Frame(marco_padre, width=250, height=250) #este y el de abajo estan contendios en el marco padre
marco.config(
    bg="blue",
    bd=5, #borde (tamaño)
    relief="solid" #relieve del borde
    #relief="raised"
)
marco.pack(side=RIGHT, anchor=SE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="yellow",
    bd=5, #borde (tamaño)
    relief="solid" #relieve del borde
    #relief="raised"
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False) #sin esto al incluir el label el marco se contrae (se hace pequeño y pierde estilo)

texto = Label(marco, text="primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    #height=10, usamos fill x y expand yes para lograr esto
    #width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(fill=Y, expand=YES)


marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue"
)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250) #este y el de abajo estan contendios en el marco padre
marco.config(
    bg="red",
    bd=5, #borde (tamaño)
    relief="solid" #relieve del borde
    #relief="raised"
)
marco.pack(side=RIGHT, anchor=SE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=5, #borde (tamaño)
    relief="solid" #relieve del borde
    #relief="raised"
)
marco.pack(side=LEFT, anchor=SW)

ventana.mainloop()