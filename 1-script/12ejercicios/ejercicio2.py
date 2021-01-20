"""
mostrar todos los numero pares del 1 al 120
"""

contador = 2

while contador <= 120:
    print(contador)
    contador+=2

print("-------------------------------------------forma2----------------------------------")

contador2= 1

for contador2 in range(1,121):
    if contador2 % 2 == 0 :
        print (contador2)
