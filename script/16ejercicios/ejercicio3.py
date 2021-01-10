"""
programa que compruebe si una variable esa  vacia, y si esta vacia rellenarla con texto en minusculas  mostrarla con texto en mayuscula
"""

texto = ""

if len(texto.strip()) <= 0:
    texto = "texto vacio"
    print(texto.upper())
else:
    print("la variable tiene contenido %" %texto)