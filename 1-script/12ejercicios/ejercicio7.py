"""
mostrar todos los numero impares del 1 al 120
"""

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if (numero1 > numero2):
    print("El numero 1 debe ser menor al numero 2")
else:
    for contador in range(numero1, (numero2 + 1)):
        if contador % 2 != 0 :
            print(contador)
