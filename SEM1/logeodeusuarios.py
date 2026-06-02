usuarios = []
while True:
    print("\n=== SAE GYM ===")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        usuario = input("Crear usuario: ")
        clave = input("Crear contraseña: ")
        usuarios.append([usuario, clave])
        print("Usuario registrado correctamente")
    elif opcion == "2":
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")
        #login de admin
        if usuario == "admin" and clave == "1234":
            print("Bienvenido dueño del gimnasio")
        else:
            encontrado = False
            for u in usuarios:
                if usuario == u[0] and clave == u[1]:
                    encontrado = True
            if encontrado:
                print("Bienvenido al gimnasio")
            else:
                print("Usuario o contraseña incorrectos")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")
