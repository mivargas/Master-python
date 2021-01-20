#condicional if------------------------------------------

print("***********************Ejemplo 1****************************")

#color = "rojo"

color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print(f"El color es {color}")
else:
    print(f"el color no es rojo, el color es {color}")


#operadores de comperacion
#  == igual
# != diferente 
# < menor que 
# > mayor que 
# <= menor igual que 
# >= mayor igual que

print("***********************Ejemplo 2****************************")

#year = 2020
year = int(input("¿En que año estamos? \n"))

if year >= 2021:
    print("estamos de 2021 en adelante")
else:
    print("es un año anterior a 2021")

print("***********************Ejemplo 3****************************")

nombre = "Miguel Vargas"

ciudad = "Caracas"

edad = 28

mayoria_edad = 18

pais = "Venezuela"

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if pais != "Venezuela":
        print("no es venezolano")
    else:
        print(f"Es venezolano de {ciudad}")
else:
    print(f"{nombre} no es  mayor de edad")


print("***********************Ejemplo 4****************************")

dia = int(input("Introduce el dia de la semana: "))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")



#operadores logicos
# and y
# or o
# ! negacion
# not no
print("***********************Ejemplo 5****************************")

edad_minima = 18
edad_maxima = 65
#edad_real = 17
edad_real = int(input("Ingrese edad: "))

if edad_real >= edad_minima and edad_real <= edad_maxima: #operador logico AND
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")


print("***********************Ejemplo 6****************************")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")


print("***********************Ejemplo 7****************************")

pais = "España"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")


print("***********************Ejemplo 8****************************")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")