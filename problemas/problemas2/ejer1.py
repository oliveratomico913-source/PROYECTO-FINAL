for curso in range(1, 5):
    asistieron =0
    faltaron=0
    for estudiantes in range(1, 7):
        asistencia=int(input("ingrese 1 si asistio, 0 si falto: "))
        if asistencia == 1:
            asistieron += 1
        else:
            faltaron += 1
            print("curso", curso)
            print("asistieron:", asistieron)
            print("faltaron:", faltaron)
print("fin")


