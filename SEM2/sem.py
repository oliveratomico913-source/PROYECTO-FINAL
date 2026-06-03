usuarios = []
clientes = []

while True:
    print("\n=== SAE GYM ===")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")

        usuarios.append([usuario, clave])
        clientes.append([usuario, "Mensual", "Pendiente"])

        print("Registro exitoso")

    elif opcion == "2":
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")

        if usuario == "admin" and clave == "1234":

            while True:
                print("\n=== ADMIN ===")
                print("1. Ver clientes")
                print("2. Actualizar pago")
                print("3. Total clientes")
                print("4. Salir")

                op = input("Opción: ")

                if op == "1":
                    for c in clientes:
                        print(c)

                elif op == "2":
                    nombre = input("Cliente: ")

                    for c in clientes:
                        if c[0] == nombre:
                            c[2] = "Al día"
                            print("Pago actualizado")

                elif op == "3":
                    print("Total:", len(clientes))

                elif op == "4":
                    break

        else:
            encontrado = False

            for u in usuarios:
                if usuario == u[0] and clave == u[1]:
                    encontrado = True

            if encontrado:
                print("Bienvenido al gimnasio")
            else:
                print("Datos incorrectos")

    elif opcion == "3":
        break