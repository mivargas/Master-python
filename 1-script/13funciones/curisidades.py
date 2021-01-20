def miFuncion(nombre): #las funciones siempre deben ir al inicio del archivo
    #print("hola que tal") #una buena practica es no usar los print dentro de las funcionas sino ratornar valores e imprimir cuando se llame la funcion
    return "hola que tal " + nombre

def miSegundaFuncion(apellido):
    return "hola que tal 2 " + apellido

nombre = "Miguel" #las variables deben estar definidas antes de llamar a la funcion nunca despues
apellido = "Vargas"

print("hola mundo")
print(f"Bienvenido {nombre}")

#miFuncion() #print de los valores devueltos no usar print dentro de la funcion
#miSegundaFuncion()

#print(miFuncion()) # usar parametros en funciones
#rint(miSegundaFuncion())

print(miFuncion(nombre)) 
print(miSegundaFuncion(apellido))