from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="HOLA SOY MIGUEL").pack(anchor=W)

imagen = Image.open("./imagenes/labsxd.png")
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack(anchor=E)
ventana.mainloop()