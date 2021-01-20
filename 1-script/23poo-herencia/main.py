import clases

persona = clases.Persona()
persona.setNombre("miguel")
persona.setApellido("Vargas")
persona.setAltura("1.70 cm")
persona.setEdad("28 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellido()}")
print(persona.hablar())

print("-------------------------------------------------------")

informatico = clases.informatico()
informatico.setNombre("Carlos")
informatico.setApellido("Martinez")
print(f"El informatico es: {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("-------------------------------------------------------")

tecnico = clases.tecnicoRedes()
tecnico.setNombre("Juan")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes()) #para heredar de una clase que ya hereda de padre (el construcotr de informatico ya que el constucctor es exclusivo de cada clase) debe especificarse en la clase la palaba super