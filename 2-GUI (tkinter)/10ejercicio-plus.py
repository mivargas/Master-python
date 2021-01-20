from tkinter import *
from tkinter import messagebox

class calculadora:

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    def sumar(self):
        try:
            self.resultado.set(float(self.numero1.get()) + float(self.numero2.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce buen los datos (usa caracteres numericos")

    def restar(self):
        self.resultado.set(float(self.numero1.get()) - float(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(float(self.numero1.get()) * float(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(float(self.numero1.get()) / float(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado: ", f"El resultado de la operacion es {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")

ventana = Tk()
ventana.title("Ejercicio completo con tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)

calculadora = calculadora(messagebox) #instancia clase, le paso la clase msbocx por marametro

marco = Frame(ventana, width=350, height=250) #se mete el formulario aqu para que no se desaliné por el incremento de tamaño (geometry)
marco.config(
    bd=5,
    relief=SOLID,
    padx=15,
    pady=15
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero: ").pack()
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()


Label(marco, text="Segundo numero: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()