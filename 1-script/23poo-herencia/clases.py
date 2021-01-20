#Herencia es la posibilidad de compartir atributos y metedos entre clases.y que diferentes clases herenden de otras
class Persona:
    """
    nombre
    apellido
    edad
    altura
    edad
    """
    
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setAltura(self, altura):
            self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar (self):
        return "Estoy hablando"
    
    def caminar (self):
        return "Estoy caminando"
    
    def dormir (self):
        return "Estoy durmiendo"
    

class informatico(Persona): #herencia
    """
    lenguajes
    experiencia
    """

    def __init__(self):
        self.lenguajes = "html, css, javascript y php"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def reparar(self):
        return "He reparado tu pc"

class tecnicoRedes(informatico): #hereda de informatico, que a suvez hereda de perdonas
    def __init__(self):
        super().__init__() #aqui llamo al metodo coontructor de informatico para poder hace uso de propiedades y metodos
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red"
