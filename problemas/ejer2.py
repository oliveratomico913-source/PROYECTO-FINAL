for categoria in range(1, 4):
    total=0
    for producto in range(1, 5):
        precio = float(input(f"precio del producto {producto} de la categoria {categoria}: "))
        total =total + precio
    print("total de la categoria",categoria, ".",total)
