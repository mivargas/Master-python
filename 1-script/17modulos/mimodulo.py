def holaMundo(nombre):
    return f"hola que tal estas {nombre}"

def calculadora(num1, num2, basicas = False):
    suma = num1+num2
    resta = num1-num2
    multi = num1*num2
    division  = num1/num2

    cadena = ""

    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena
