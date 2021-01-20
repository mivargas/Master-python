from io import open
import pathlib #ruta absoluta
import shutil # copiar, renombrar y mover  archivos

#abrir archivo (abrir y/o crear)
#archivo = open("./19sistemas-archivos/fichero_texto.txt", "a+")
#archivo = open(pathlib.Path().absolute() + "fichero_texto.txt", "a+") #ruta absluta


ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt" 
#print(ruta)
archivo = open(ruta, "a+") #ruta absluta en conjunto de lo de arriba

#escribir
archivo.write("***********soy un texto metido desde python**************\n")

#cerrar
archivo.close() #cerrar el archivo ya abierto (se deben cerrar los aarchivos al terminar de escribir o hacer cualquier cambio)




#abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt" 
archivo_lectura = open(ruta, "r") 

#leer contenido
#contenido = archivo_lectura.read()
#print(contenido) #mostar todo el contenido completo

#leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
#print(lista)

for frase in lista:
    if not frase.isnumeric(): #mostrar miestras grase no sea numerico
        print(f"- {frase.upper()}") #upper es para mayusculas
    
        lista_frase = frase.split() #crar lista por cada elemento
        print(lista_frase) #capitalize() si quiero la primera letra en mayuscula y center(100) si qquiero centrar el texto


#copiar
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt" 
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"  #copiar y asignar nuevo nombre
shutil.copyfile(ruta_original, ruta_nueva)

#mover
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt" 
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copiado_NUEVO.txt"  #ccambiar nombre
shutil.move(ruta_original,ruta_nueva)

#eliminar
import os

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copiado_NUEVO.txt"  #ccambiar nombre
os.remove(ruta_nueva)

#comprobar si un un archivo existe
#print(os.path.abspath("./"))# me da la ruta absoluta
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
if os.path.isfile(ruta_comprobar):
    print("el archivo existe")
else:
    print("el archivo no existe")