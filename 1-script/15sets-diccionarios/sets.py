"""
set tipo de dato para tener una coleccion de valores pero no tiene ni idice ni orden

"""

personas = {
    "victor",
    "manolo",
    "francisco"
}

personas.add("paco")
personas.remove("francisco")
print(personas)
print(type(personas))