# for variable in elemento_iterable (lista, rango, etc)

contador = 0
resultado = 0

for contador in range(0,10):
    print("voy por el %s" %contador) 
    
    resultado += contador # igual que decir resultado = resultado + contador

print(f"el resultado es: {resultado}")

numero_usuario = int(input("Introduce numer a multiplicar: "))

if numero_usuario < 1:
    numero_usuario = 1

print("\n####Tabla del nimero %s####" %numero_usuario)

for numero_tabla in range(1,11):
    if numero_usuario ==45:
        print("No se puede mostrar numero prohibido")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print(f"tabla del {numero_usuario} finalizada") #python permite else en los for para una adicioanrl algo al cerrar el ciclo
