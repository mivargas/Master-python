import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    
    def registro(self):
        print("\nVamos a registrarte en el sistema...")
        nombre = input("¿Cual es tu nombre?: ")
        apellido = input("¿Cual es tu apellido?: ")
        email = input("¿Cual es tu email?: ")
        password = input("¿Cual es tu contraseña?: ")

        usuario = modelo.usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("\nIdentificate en el sistema...")
        try:
            email = input("¿Cual es tu email?: ")
            password = input("¿Cual es tu contraseña?: ")
            usuario = modelo.usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registado en el sitema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto intentalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear notas (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl  = notas.acciones.Acciones()

        if accion == "crear":
            #print("vamos a crear")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "mostrar":
            #print("vamos a mostrar")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "eliminar":
            #print("vamos a eliminar")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "salir":
            print(f"ok {usuario[1]}, hasta pronto")
            exit()
        
        else:
            print("Opcion invalida vuelva a intentar")
            self.proximasAcciones(usuario)
        