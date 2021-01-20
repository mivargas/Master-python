"""
escribir un programa que añada valores a una lista mientras que su lonjitud sea menor a 120  y mostarla
usar  while y for
"""

lista = []

for elemento in range(120):
    lista.append(elemento)

print(lista)
print("\n------------------------------------------------")

lista2 = []
i = 0
while i < 120:
    lista2.append(i)
    i+=1
print(lista2)
