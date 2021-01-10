"""
4 variables: una lista un string un entero y un booleano y que imprima un mensaje segun el tipo de dato de cada variable
"""

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CAMPO DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"
    
    return result

def comprobaTipado(dato, tipodato):
    comprobar = isinstance(dato, tipodato)
    result = ""

    if comprobar:
        #result = f"Es te dato es de tipo {type(dato)}"
        result = f"Es te dato es de tipo {traducirTipo(tipodato)}"
    else:
        result = "El tipo de  dato no es corecto"
    
    return result

mi_lista = [1,5,6,8]
mi_string = "esto es un string"
mi_entero = 3
mi_bool = True

print(comprobaTipado(mi_lista, list))



