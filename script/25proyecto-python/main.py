"""
-Abrir asistente 
-login o registro
-si es registro, creara usuario
-si es login identifica el usuario y lanza otro asistente
-crear nota, mostras notas, borrar notas
"""
from usuarios import acciones

#con triple comilla podemos hacer saltos de linea sin importar tabulacion 
print("""
Acciones disponibles:
    - registro
    - login
""")

hazEl=acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
else:
    print("Opcion invalida intente mas tarde")