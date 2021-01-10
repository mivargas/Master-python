class Coche:

    #atributos o propiedades (variales)
    #caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "Hola, soy un atributo público"
    __soy_privado = "Hola, soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
    
    #metodos son acciones que hace el objeto (funciones)

    #Getters y setters
    def getPrivado(self):
        return self.__soy_privado
        
    def setColor(self, color):
        self.color = color #self es el equivalente al this en otros lenguajes
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def acelerar(self): #self para acceder a las propiedades de la clase
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad    

    def getInfo(self):
        info = "-------Información del conche------"
        info+= "\nColor: " + self.getColor()
        info+= "\nMarca: " + self.getMarca()
        info+= "\nModelo: " + self.getModelo()
        info+= "\nVelocidad: " + str(self.getVelocidad())

        return info

#fin definicion clase