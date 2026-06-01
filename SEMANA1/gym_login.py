usuario_correcto = "oliveratom"
clave_correcta = "soyelmejor7R"
print("BIENVENIDO A SAE GYM")
while True:
# Entrada de datos
    usuario = input("Ingrese usuario: ")
    clave = input("Ingrese contraseña: ")

    # Validación
    if usuario == usuario_correcto and clave == clave_correcta:
        print("\nAcceso permitido")
        break
    else:
        print("\nUsuario o contraseña incorrectos")
        print("Intente nuevamente\n")
print(" SISTEMA SAE GYM")
# Menú principal
while True:
    print("\nMENU PRINCIPAL")
    print("1. Registrar cliente")
    print("2. Ver clientes")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    # Opciones
    if opcion == "1":
        nombre = input("Ingrese nombre del cliente: ")
        print(f"Cliente {nombre} registrado correctamente")
    elif opcion == "2":
        print("Lista de clientes no disponible")
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")