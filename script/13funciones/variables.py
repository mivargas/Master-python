#variables locales y globales

#local solo disponible dentro de la uncion
#global disponibles dentro y fuera de la funcion

frese = "Ni los genios son tan genios, ni los mediocres tan mediocres!" #variable global
print(frese)

def holaMundo():
    frase = "Hola mundo" #variable local si se comentara mostraria el contenido de la variable global frase global
    print(frase)

    year = 2021
    print(year)
    
    global correo #convertir variable local en global
    correo = "miguelvargas619@gmail.com"
    print(f"dentro: {correo}")

    return f"Dato devuelto: {year}" #manera de devolver una variable local para su uso
print(holaMundo())
print(f"fuera: {correo}") #variable que fue convertida en global dentro de la funcion 
#print(year) #esto no funcionara puesto que la variable es local, para poder acceder a el en todo caso al ser local debe usarse un return

