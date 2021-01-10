nombre = "Miguel Vargas"

print(type(nombre)) #print imprime y type me dice el tipo de ariable

comprobar = isinstance(nombre, str) #comprueba la instacia en tipo de variable para comprovar (devuelve true o false)

if comprobar: #validamos (devolvio True)
    print("es un string")
else:
    print("no es una cadena")

if not isinstance(nombre, float):
    print("la variable no es un numero con decimales")

#limpiar espacios
frase = "      mi contenido        "
print(frase)
print(frase.strip()) # sin espaion

#eliminar variables
year = 2021
#del year #borrada y no servira en el print
print(year)

#comprobar variable vacia
texto = "    hola   "

if len(texto) <= 0:
    print("la  variable esta vacia") 
else:
    print(f"la variable tiene contenido {len(texto)}")

#encontrar caracteres 
frase = "la vida es bella"

print(frase.find("vida")) # a partir del caracter 3

#remplazar palabras en string

nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())