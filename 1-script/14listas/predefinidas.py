cantantes = ["drake", "talia", "big ariana", "Sia"]
numeros = [1,2,5,8,3,4]

#ordenar lista
print(numeros)
numeros.sort()
print(numeros)

#añadir elementos en una posicion especifica
cantantes.insert(3, "reik")
print(cantantes)

#eliminar elementos
cantantes.pop(1) #por indice
cantantes.remove("reik") #por valor
print(cantantes)

#dar la vuelta
numeros.reverse()
print(numeros) 

#buscar dentro de una lista
print("big ariana" in cantantes)

#contar elementos
print(cantantes)
print(len(cantantes))

#cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

#conseguir el indice
print(cantantes.index("Sia"))

#unir listas
cantantes.extend(numeros)
print(cantantes)