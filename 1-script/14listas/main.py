"""
listas (arrays)
"""

pelicula = "Batman"

#definir lista:
peliculas = ["batmas", "spiderma", "el señor de los anillos"]
cantantes = list(("drake", "rihana", "juan gabriel")) #segunda forma de definir lista funcion lis() pero hay que pasarle tupla dentro
years = list(range(2020, 2050)) #rango de año
variada = ["Miguel", 39, 12.4, True, "texto"]

print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)

#indices
print(peliculas[1]) #acceder a un indice 
print(peliculas[-2]) #indices en negativo (desde atras hacia adelante)
print(cantantes[1:3]) #intervalo a devolver de la lista (una especie de sublista)
print(cantantes[0:1])
print(cantantes[0:2])
print(cantantes[1:]) #mostrar todo de la posicion 1 en adelante
print(cantantes[:2]) # todo hasta la posicion 2

#añadir elementos a una lista
cantantes.append("SIA")
cantantes.append("Big Ariana")
print(cantantes)

#recorrer lista

#ejemplo while opcional
nueva_pelicula = None
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce nueva pelicula: ")
    if nueva_pelicula == "parar":
        break
    peliculas.append(nueva_pelicula)

print("\n######listado de peliculas########")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")


#listas multidimensionales
print("\n######listado de contactos########")
contactos = [
    [
        "antonio",
        "antonio@a.com"
    ],
    [
        "luis",
        "luis@a.com"
    ],
    [
        "salvador",
        "salvador@a.com"
    ],

]

print(contactos)

print(contactos[1][1]) #acceder a elementos de listas multidimecionales

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Apellido: " + elemento)
    print("\n")