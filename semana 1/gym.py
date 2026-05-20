# =========================================
# PROYECTO FINAL - SISTEMA DE GIMNASIO
# AVANCE 1
# =========================================

# Datos de acceso
usuario_correcto = "admin"
clave_correcta = "gym123"

print("===================================")
print("     BIENVENIDO A TITAN GYM")
print("===================================")

# Bucle de seguridad
while True:

    # Entrada de datos
    usuario = input("Ingrese usuario: ").strip().lower()
    clave = input("Ingrese contraseña: ").strip()

    # Validación
    if usuario == usuario_correcto and clave == clave_correcta:
        print("\nAcceso permitido")
        break
    else:
        print("\nUsuario o contraseña incorrectos")
        print("Intente nuevamente\n")

# Pantalla principal
print("\n===================================")
print("     SISTEMA TITAN GYM")
print("===================================")

# Menú principal
while True:

    print("\nMENU PRINCIPAL")
    print("1. Registrar cliente")
    print("2. Ver clientes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ").strip()

    # Opciones
    if opcion == "1":
        nombre = input("Ingrese nombre del cliente: ").strip().title()
        print(f"Cliente {nombre} registrado correctamente")

    elif opcion == "2":
        print("Lista de clientes próximamente...")

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")