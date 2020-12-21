"""
mostrar el porcetaje de un numero solicitado por el usuario
"""

numero = int(input("Introduce el numero: "))
porcetaje = int(input(f"Introduce el % para {numero}: "))

print(f"el {porcetaje}% de {numero} es {(porcetaje//100)}")
