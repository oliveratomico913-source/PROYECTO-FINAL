for aula in range(1, 5):
    suma=0
    for estudiante in range(1, 6):
        nota =float(input(f"nota del estudiante {estudiante} del aula {aula}: "))
        suma =suma +nota
        promedio = suma/ 5
    print("promedio final del aula",aula, ":",promedio)
        



