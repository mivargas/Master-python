"""
proyecto, que tenga:
-una ventana
-tamaño fijo de la ventana
-ventana no redimensionable
-un menu (inicio, añadir, informacion, salir)
-diferentes pantallas
-formulario de añadir productos
-guardar datos temporalemente
-mostrar datos listados en la pantalla principal
-opcion e salir
"""

from tkinter import *
from tkinter import ttk

#definir ventana
ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500, 500)# tamaño minimo base y se adapta cuando hay mas datos
ventana.title("Proyecto tkinter")
ventana.resizable(0,0)

#pantallas
def home():
    #montar pantallas
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=80,
        pady=20
    )
    home_label.grid(row=0, column=0)
    
    products_box.grid(row=1)

    #listar productos
    """
    for product in products:
        if len(product) == 3:
            product.append("added") #solomuestra cuando se actualiza la lista y no los anteriores
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="--------------------------").grid()
    """

    #con treeview
    for product in products:
        if len(product) == 3:
            product.append("added") #solomuestra cuando se actualiza la lista y no los anteriores
            products_table.insert('', 0, text=product[0], values = (product[1]))
    #ocultar pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def add():
    #encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=80,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=4)
    #mis campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_desc_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    add_desc_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_desc_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15, 
        pady=15
    )
    add_separator.grid(row=4)
    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )
    #ocultar pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=80,
        pady=20
    )
    info_label.grid(row=0, column=0)
    #ocultar pantallas
    home_label.grid_remove()    
    add_frame.grid_remove()
    add_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

data_label= Label(ventana, text="Creado por miguel")
data_label.grid(row=1, column=0)

def add_products():
    products.append([
        name_data.get(),
        price_data.get(),
        add_desc_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_desc_entry.delete("1.0", END)
    #print(products)
    home()

#variables importantes
products = []
name_data = StringVar()
price_data = StringVar()

#campos del formulario
add_frame =Frame(ventana) #util para ocultar el formulario y no ir uno a uno por elemento

add_name_label=Label(add_frame, text="Nombe del prducto:")
add_name_entry= Entry(add_frame, textvariable=name_data)

add_price_label=Label(add_frame, text="Precio del prducto:")
add_price_entry= Entry(add_frame, textvariable=price_data)

add_desc_label=Label(add_frame, text="Descripcion del prducto:")
add_desc_entry= Text(add_frame)

add_separator=Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_products)


#definir campos de pantallas
home_label = Label(text="Inicio")
products_box = Frame(ventana, width=250)

Label(products_box).grid(row=0)
products_table = ttk.Treeview(height=12, columns=2)
products_table.grid(row=1, column=0, columnspan=2)
products_table.heading("#0", text="Producto", anchor=W)
products_table.heading("#1", text="Precio", anchor=W)


add_label = Label(text="Añadir")
info_label = Label(text="Informacion")

#cargar pantalla inicio
home()

#menu superior
menu_superior= Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="añadir", command=add)
menu_superior.add_command(label="informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#cargar menu
ventana.config(menu=menu_superior)






#cargar ventana
ventana.mainloop()