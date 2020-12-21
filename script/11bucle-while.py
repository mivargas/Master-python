"""
while expression:
    bloque de intrucciones
    actualizar contador
"""

contador = 1

while contador <= 100:
    print(f"Estoy en el numero {contador}")
    contador+=1

print("------------------------------------------")

contador2 = 1

muestrame = str(0)

while contador2 <= 100:
    muestrame = muestrame + "," + str(contador2)
    contador2+=1

print(muestrame)

print("------------------------------------------")

numero_usuario = int(input("Introduce numer a multiplicar: "))

if numero_usuario < 1:
    numero_usuario = 1

print("\n####Tabla del nimero %s####" %numero_usuario)

contador3 = 1

while contador3 <= 10:
    print(f"{numero_usuario} x {contador3} = {numero_usuario * contador3}")
    contador3 += 1
else:
    print("Tabla terminada")