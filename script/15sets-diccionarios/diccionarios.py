"""
es como array asociativo  (clave - valor)
"""

persona = {
    "nombre":"miguel",
    "apellido":"vargas",
    "correo":"miguelvargas@gmail.com"
}

print(persona)
print(type(persona))

print(persona["apellido"])

#lista con diccionarios

contactos = [
    {
        "nombre":"miguel",
        "email":"miguel@gmail.com"
    },
    {
        "nombre":"luis",
        "email":"luis@gmail.com"
    },
    {
        "nombre":"juan",
        "email":"juan@gmail.com"
    }

]

print(contactos)

#acceder 
print(contactos[0]["nombre"])

#modificar valores de propiedad
contactos[0]["nombre"] ="miguelito"
print(contactos)

print("\nListado")

for contacto in contactos:
    print("Nombre: %s" %contacto["nombre"])
    print(f"Email: {contacto['email']}")
    print("--------------------------------")
