"""
hacer una lista que tenga 8 numeros enteros 
se debe recorrer (sin funcion y una con funcion) 
mostrar ordenar
mostrar su lonjutud
buscar elemento que el usuario pida por teclado
"""
#crear
lista = [5, 2, 7, 4, 8, 6, 1, 9]

#recorrer
print("\n-------------------recorrer-------------------------")
for elemento in lista:
    print(elemento)

#recorrer con funcion
print("\n-------------------recorrer con funcion-------------------------")

def recorrerLista(miLista):
    cadena =""
    for recorrido in miLista:
        cadena+=str(recorrido)
        cadena+="\n"
    return cadena

print(recorrerLista(lista))
#print(recorrerLista(["maria", "juan", "pepe"]))

#ordenado
print("\n-------------------mostrar ordenado-------------------------")
lista.sort()
print(lista)

#longitud
print("\n-------------------mostrar longitud-------------------------")
print(f"{len(lista)} elementos")

#buscar elemento
print("\n-------------------mostrar elemento buscado-------------------------")
buscar = int(input("ingresa numero a buscar: "))
#print(buscar in lista)

comprobar = isinstance(buscar, int)

while not comprobar or buscar <= 0:
    buscar = int(input("ingresa numero a buscar: "))
else:
    print("has introducido el %s" %buscar)

print("#######Buscar en la lista el número {}#########".format(buscar))

searh = lista.index(buscar)
print("el numero buscado existe en la lista es e indice " +str(searh))
