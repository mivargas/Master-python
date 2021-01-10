#programacion orientada a objetos


#definir una clase(molde para crear mas objetos de ese tipo)
#(Coche) con caracteristicas similares

class Coche:

    #atributos o propiedades (variales)
    #caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    
    #metodos son acciones que hace el objeto (funciones)

    #Getters y setters
    def setColor(self, color):
        self.color = color #self es el equivalente al this en otros lenguajes
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self): #self para acceder a las propiedades de la clase
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad    

#fin definicion clase

#crear objeto / instanciar la clase
coche = Coche()
print("COCHE1: ")
coche.setColor("amarillo")
coche.setModelo("murcielago")
print(coche.getColor(), coche.getModelo())

print(coche.marca, coche.color)
#print(f"Velocidad actual: {coche.velocidad}") #se recomienda no interactuar directamente con las propiedades (usar set y get)
#print(f"Velocidad actual: {coche.velocidad}")
print(f"Velocidad actual: {coche.getVelocidad()}")


coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
#print(f"Velocidad actual: {coche.velocidad}")
print(f"Velocidad actual: {coche.getVelocidad()}")

coche.frenar()
#print(f"Velocidad actual: {coche.velocidad}")
print(f"Velocidad actual: {coche.getVelocidad()}")

print("----------------------------------")
#crear mas objetos (misma clase objetos con diferentes caracteristicas(reutilizacion de codigo))
print("COCHE2: ")
coche2 = Coche()
print(coche2.getColor())
coche2.setColor("Verde")
coche2.setModelo("Gallardo")
print(coche2.getColor(), coche2.getModelo())
