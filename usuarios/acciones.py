import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")

        nombres = input("¿Cuales son tus nombres?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Digita tu email: ")
        password = input("Digita tu contraseña: ")

        usuario = modelo.Usuario(nombres, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"\nPerfecto {registro[1].nombres} te has registrado con el email {registro[1].email}"
            )

        else:
            print("\nNo te has registrado correctamente!!")

    def login(self):
        print("\nVale!! Identificate en el sistema...")

        try:

            email = input("Digita tu email: ")
            password = input("Digita tu contraseña: ")

            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(
                    f"\nBienvenid@ {login[1]}, ha ingresado correctamente en el sistema el {login[5]}"
                )
                self.proximasAcciones(login)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"\nOk {usuario[1]}, hasta pronto!!!...")
            exit()

