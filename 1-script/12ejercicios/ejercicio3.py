"""
mostart los cuadrados (numero multiplicado por si mismo)
"""

#while
contador = 0

while contador <= 60:

    cuadrado = contador*contador
    print(f"el cuadrado de {contador} es {cuadrado}")

    contador+=1

#for
for numero in range(61):
    numcuadrado= numero*numero
    print(f"el cuadrado de {numero} es {numcuadrado}")