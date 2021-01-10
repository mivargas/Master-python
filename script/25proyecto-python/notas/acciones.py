import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"\nOk {usuario[1]} vamos a crear una nueva nota")

        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1: #esto es o que se encuantra en el retorno de return [cursor.rowcount, self] especificamente de rowcount si el conteo en mayor a uno fue exitoso el self contine os datos del objeto que se guardo
            #print(nota)
            #print(guardar[1])
            print(f"Perfecto has guardado la nota {nota.titulo}")
        else:
            print(f"no se ha guardado la nota lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"Ok {usuario[1]} aqu tienes tus notas")

        nota = modelo.Nota(usuario[0])
        notas =nota.listar()
        #print(notas)

        for mi_nota in notas:
            print("\n********************************************")
            print(mi_nota[2])
            print(mi_nota[3])

    def borrar(self, usuario):
        print(f"Ok {usuario[1]} vamos a borrar notas")
        titulo = input("ingresa titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.elminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print("NO se ha podido borrar la nota. intenta mas tarde...")
