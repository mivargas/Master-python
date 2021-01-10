#capturar excepciones y manejar errores
try: #inicio de declaracion de manejo de errores
    nombre = input("ingrese el nombre: ")
    if len(nombre) > 1:
        nombre_user = ("El nombre es "  + nombre)
    print(nombre_user)
except: #en otros lenguajes se conoce como catch
    print("ha ocurrido un error ingresa bien el nombre")
else:
    print("todo ha funcionado perfectamente") #si todo va bien sin errores se muestra
finally:
    print("fin del programa") # se muestra al final de la ejecucion haya o no errores

"""
lista = [5, 2, 7, 4, 8, 6, 1, 9]
buscar = int(input("ingresa numero a buscar: "))
comprobar = isinstance(buscar, int)

while not comprobar or buscar <= 0:
    buscar = int(input("ingresa numero a buscar: "))
else:
    print("has introducido el %s" %buscar)

print("#######Buscar en la lista el número {}#########".format(buscar))

try:
    searh = lista.index(buscar)
    print("el numero buscado existe en la lista es e indice " +str(searh))
except:
    print(f"no existe el elemento {buscar} en la lista")
"""

#multiple excepciones

"""
try:
    numero = int(input("dime el numero a elevarlo al cuadrado: "))
    print("el cuadrado es " + str(numero*numero))
except TypeError:
    print("debes convertir tus cadenas a enteros para multiplicar")
#except ValueError:
#    print("introduce un numero correcto")
except Exception as e:
    print(type(e))
    print("ha ocurrido un error: ", type(e).__name__)
"""

#excepciones personalizadas (o lanzar excepcion)
"""
nombre = input("introduce el nombre: ")
edad = int(input("introduce la edad: "))

if edad < 5 or edad >110:
    raise ValueError("Edad introducioda no es real") #se usa el raise para y el tipo de error que quiero lanzar
elif len(nombre) <=1:
    raise ValueError("El nombre no esta completo")
else:
    print("bienvenido al paster de pytho " + nombre)
 """

"""mostrar errores mas limpios"""
try:
    nombre = input("introduce el nombre: ")
    edad = int(input("introduce la edad: "))

    if edad < 5 or edad >110:
        raise ValueError("Edad introducioda no es real") 
    elif len(nombre) <=1:
        raise ValueError("El nombre no esta completo")
    else:
        print("bienvenido al paster de python " + nombre)
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error ", e) # si hay un error diferente a ValueError mostrara esto