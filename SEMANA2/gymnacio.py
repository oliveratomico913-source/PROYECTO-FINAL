usuario_correcto = "oliveratom"
clave_correcta = "soyelmejor7R"
clientes = []
print("BIENVENIDO A SAE GYM")
while True:
    usuario = input("Ingrese usuario: ")
    clave = input("Ingrese contraseña: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("\nAcceso permitido")
        break
    else:
        print("\nUsuario o contraseña incorrectos")
        print("Intente nuevamente\n")
print("SISTEMA SAE GYM")
while True:
    print("\nMENU PRINCIPAL")
    print("1. Registrar cliente")
    print("2. Ver clientes")
    print("3. Buscar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese nombre del cliente: ")
        pago = input("¿Pagó mensualidad? (si/no): ")
        cliente = {
            "nombre": nombre,
            "pago": pago
        }
        clientes.append(cliente)
        print(f"Cliente {nombre} registrado correctamente")
    elif opcion == "2":
        if len(clientes) == 0:
            print("No hay clientes registrados")
        else:
            print("\nLISTA DE CLIENTES")
            for cliente in clientes:
                print(f"Nombre: {cliente['nombre']} | Mensualidad: {cliente['pago']}")
    elif opcion == "3":
        buscar = input("Ingrese nombre a buscar: ")
        encontrado = False
        for cliente in clientes:
            if cliente["nombre"].lower() == buscar.lower():
                print("\nCLIENTE ENCONTRADO")
                print(f"Nombre: {cliente['nombre']}")
                print(f"Mensualidad: {cliente['pago']}")
                encontrado = True
        if not encontrado:
            print("Cliente no encontrado")
    elif opcion == "4":
        eliminar = input("Ingrese nombre a eliminar: ")
        encontrado = False
        for cliente in clientes:
            if cliente["nombre"].lower() == eliminar.lower():
                clientes.remove(cliente)
                print("Cliente eliminado correctamente")
                encontrado = True
                break
        if not encontrado:
            print("Cliente no existe")
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")