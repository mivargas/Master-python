"""
def nombreDeMiFuncion(parametros):
    bloque de instrucciones

nombreDeMiFuncion(mi_parametro)
"""

#ejemplo 1
print("#####Ejemplo 1#####")

def muestraNombres():
    print("Miguel")
    print("Adriana")
    print("Juan")
    print("Maria")
    print("Samuel")
    print("\n")

# invocar función:
muestraNombres()
muestraNombres()
muestraNombres()

#ejemplo 2 parametros
print("#####Ejemplo 2#####")


def mostarTuNombre(nombre, edad):
    print("Tu nombre es %s" %nombre)
    if edad > 17:
        print("Y es mayor de edad")
#mostarTuNombre("Miguel Vargas")
#mostarTuNombre("Sandra Cogola")
#mostarTuNombre("David Picaso")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostarTuNombre(nombre, edad)


#ejemplo 3
print("#####Ejemplo 3#####")

def tabla(numero):
    print(f"Tabla de multiplicar de numero: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

tabla(3)
tabla(7)

print("----------------------------")
for numero_tabla in range(1,11):
    tabla(numero_tabla)

#ejemplo 4 parametros opcionales
print("#####Ejemplo 4#####")

def getEmpleado(nombre, cedula = None): #parametro opcional por defecto se coloca none
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if cedula != None: #evitar mostar si el parametro es opcional
        print(f"Cedula: {cedula}")

getEmpleado("Miguelvargas")

#ejemplo 5 parametros opcionales y devolver datos
print("#####Ejemplo 5#####")

def saludame(nombre):
    saludo = f"hola saludos {nombre}"

    return saludo

print(saludame("Miguel"))

#ejemplo 6
print("#####Ejemplo 6#####")

def calculadora(num1, num2, basicas = False):
    suma = num1+num2
    resta = num1-num2
    multi = num1*num2
    division  = num1/num2

    cadena = ""

    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

#print(calculadora(5,5))
print(calculadora(5,5, True))

#ejemplo 7 ejemplo de funciones dentro de funciones
print("#####Ejemplo 7#####")

def getNombre(nombre):
    texto = f"El nombre del usuario es {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos del usuario son {apellidos}"
    return texto
def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Miguel", "Vargas R"))
#print(getNombre("Miguel"), getApellidos("Vargas R"))


#ejemplo 8 funciones lambda (anonimas, para funciones simples y pequeñas)
print("#####Ejemplo 8#####")

dime_el_year = lambda year: f"El año es {year * 50}" #year es el parametro, todo se tiene que definir en una sola linea

print(dime_el_year(2034))