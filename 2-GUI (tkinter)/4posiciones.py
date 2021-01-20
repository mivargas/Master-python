from tkinter import *

ventana = Tk()
#ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white", #color de letra
    bg="black", #color del foondo (se puede usar codigo hexadecimales)
    padx=20, #espaciado horizontal (pading)
    pady=20,
    font=("Arial", 20) #letra
)
texto.pack(side=TOP)

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
texto.pack(side=TOP, fill=X, expand=YES)#pocisionado arriba y el fill se usa en conjunto con el expand para saber si se expandira en el eje x o en el eje y


texto = Label(ventana, text="Basico1")
texto.config(
    #width=400,#acho de elemento
    #height=400, #alto
    bg="green", #me ayuda a ubicarme donde esta el elemnto
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle" #cambia el cursor cuando este encima del elemento 
    
)
texto.pack(side=LEFT, fill=X, expand=True)#asi colocamos uno al lado del otro empezando por la izquierda
texto = Label(ventana, text="Basico2")
texto.config(
    #width=400,#acho de elemento
    #height=400, #alto
    bg="red", #me ayuda a ubicarme donde esta el elemnto
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle" #cambia el cursor cuando este encima del elemento 
    
)
texto.pack(side=LEFT, fill=X, expand=True)

texto = Label(ventana, text="Basico3")
texto.config(
    #width=400,#acho de elemento
    #height=400, #alto
    bg="pink", #me ayuda a ubicarme donde esta el elemnto
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle" #cambia el cursor cuando este encima del elemento 
    
)
texto.pack(side=LEFT, fill=X, expand=True)

ventana.mainloop()