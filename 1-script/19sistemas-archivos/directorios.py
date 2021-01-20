import os
import shutil
#crear carpeta

if not os.path.isdir("./mi_carpeta"): #es recomendable usar una ruta absoluta. Esta es una manera mas simple pero menos segura(ruta relativa)
    os.mkdir("./mi_carpeta")
else:
    print("ya existe el directorio")

"""
#eliminar carpeta
os.rmdir("mi_carpeta")

#copiar
ruta_original = "./mi_carpeta" 
ruta_nueva = "./mi_carpeta_COPIADA"  #copiar y asignar nuevo nombre
shutil.copytree(ruta_original, ruta_nueva)
"""

#listar
print("contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")
print(contenido)

for fichero in contenido:
    print("fichero: " +fichero)