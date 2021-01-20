"""
los paquetes son un conjunto de modulos agrupados dentro de un directorio
para decirle a un directorio que sera un paquete se debe crear un archivo en blanco con el nombre __init__.py
"""
print("PROBANDO PAQUETES:")

from mipaquete import pruebas #forma de importar paquetes
from mipaquete import herramientas
#from mipaquete import pruebas, herramientas #forma corta de importacion

pruebas.probando()
herramientas.nombreCompleto("Miguel", "Vargas")

"""
https://pypi.org/
sitio oficial de paquetes de python. Se pueden encotrar para generar PDF, hacer chats, etc... (pueden encontrarse paquetes o modulos simples)
"""