from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "Sead", "Panda", 240, 150, 4)
carro2 = Coche("Azul", "citraen", "Zara", 100, 180, 4)
carro3 = Coche("Gris", "Mercedez", "Clase A", 400, 350, 4)

print(carro.getColor())

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#detectar tipado de objeto
if type(carro3) == Coche: #se compara con la clase 
    print("Es un objeto correcto")
else:
    print("no es un objeto")

#visivilidad
print(carro.soy_publico)
#print(carro.__soy_privado) #falla porque es privado solo se  puede acceder con un get
print(carro.getPrivado())