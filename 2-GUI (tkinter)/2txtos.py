from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white", #color de letra
    bg="black", #color del foondo (se puede usar codigo hexadecimales)
    padx=20, #espaciado horizontal (pading)
    pady=20,
    font=("Arial", 20) #letra
)
texto.pack()

texto = Label(ventana, text="SOY MIGUEL")
texto.config(
    #width=400,#acho de elemento
    #height=400, #alto
    bg="orange", #me ayuda a ubicarme donde esta el elemnto
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle" #cambia el cursor cuando este encima del elemento 
    
)
texto.pack(anchor=SE)#pocisionar norte, sur, este u oeste n,s,e,w


texto = Label(ventana, text="Master en python")
texto.config(
    #width=400,#acho de elemento
    #height=400, #alto
    bg="orange", #me ayuda a ubicarme donde esta el elemnto
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle" #cambia el cursor cuando este encima del elemento 
    
)
texto.pack(anchor=SW)#pocisionar norte, sur, este u oeste n,s,e,w

ventana.mainloop()