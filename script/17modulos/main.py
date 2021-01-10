"""
Son funcionalidades ya hechas para reutilzar (conocido como librerias en otros lenguajes)
https://docs.python.org/3/py-modindex.html

pedemos conseguir modulos en internet o crearlos nosotros mismos
"""

#importar modulo propio
import mimodulo #importar todo el modulo (todas las funciones)

print(mimodulo.holaMundo("miguel"))

print(mimodulo.calculadora(3, 5, True))

"""
from mimodulo import calculadora # importar una sola funcion del modulo
print(calculadora(3, 5, True))
"""

"""
from mimodulo import * # importar todas sin tener modulo delante en el nombre pero debe usarse si van a hacerse uso de todas las funciones (recomendacion)
print(holaMundo("miguel"))
print(calculadora(3, 5, True))
"""

#modulo fechas
import datetime #modulo de python 

print(datetime.date.today())

fechas_completa = datetime.datetime.now()
print(fechas_completa)
print(fechas_completa.year)
print(fechas_completa.month)
print(fechas_completa.day)

fecha_personalizada = fechas_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)

print(datetime.datetime.now().timestamp())

print(datetime.datetime.now().time())


#modulo matematicas
import math #modulo de python

print("la raiz cuadrada de 10:", math.sqrt(10))

print("numero pi:", math.pi)

print("numero pi:", float(math.pi)) # convirtiendo el dato de str a float

print("redondear", math.ceil(5.678))
print("redondear", math.floor(5.678))

#Modulo random

import random

print("numero aleatorio entre 15 y 67: ", random.randint(15,67))