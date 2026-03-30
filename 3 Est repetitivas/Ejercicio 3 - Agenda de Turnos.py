while True:
    operador = input("Ingrese el nombre del operador: ").capitalize()
    if operador.isalpha():
        break
    else:
        print("Error: ingrese solo letras")


lunes1 = "Libre"
lunes2 = "Libre"
lunes3 = "Libre"
lunes4 = "Libre"

martes1 = "Libre"
martes2 = "Libre"
martes3 = "Libre"

while True:
    print("Menú\n"
          "1-Reservar Turno\n"
          "2-Cancelar turno (por nombre)\n"
          "3-Ver agenda del día\n"
          "4-Ver resumen general\n"
          "5-Cerrar sistema\n")

    while True:
        opcion = input("Ingrese una opción: ")
        if not opcion.isdigit():
            print("Ingrese un número válido")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 5:
            print("Ingrese una opción válida")
            continue
        break

    match opcion:
        case 1:
            while True:
                dia = input("Eliga el día: Lunes=1 y Martes=2: ")
                if not dia.isdigit():
                    print("Ingrese 1 si quiere reservar un turno el día Lunes o 2 si quiere reservar un turno el día Martes")
                    continue
                dia = int(dia)
                if dia not in [1, 2]:
                    print("Ingrese 1 si quiere reservar un turno el día Lunes o 2 si quiere reservar un turno el día Martes")
                    continue
                else:
                    break

            while True:
                nombre_paciente = input("Ingresar nombre paciente: ")
                if nombre_paciente.isalpha():
                    break
                else:
                    print("Ingrese un nombre válido")

            if dia == 1:
                if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                    print(f"El paciente {nombre_paciente} ya posee un turno")
                elif lunes1 == "Libre":
                    lunes1 = nombre_paciente
                    print("Se reservo para el 1er turno del Día Lunes")
                elif lunes2 == "Libre":
                    lunes2 = nombre_paciente
                    print("Se reservo para el 2do turno del Día Lunes")
                elif lunes3 == "Libre":
                    lunes3 = nombre_paciente
                    print("Se reservo para el 3er turno del Día Lunes")
                elif lunes4 == "Libre":
                    lunes4 = nombre_paciente
                    print("Se reservo para el 4to turno del Día Lunes")
                else:
                    print("No hay turno para el día Lunes")
            elif dia == 2:
                if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                    print(f"El paciente {nombre_paciente} ya posee un turno")
                elif martes1 == "Libre":
                    martes1 = nombre_paciente
                    print("Se reservó para el 1er turno del Día Martes")
                elif martes2 == "Libre":
                    martes2 = nombre_paciente
                    print("Se reservó para el 2do turno del Día Martes")
                elif martes3 == "Libre":
                    martes3 = nombre_paciente
                    print("Se reservó para el 3er turno del Día Martes")
                else:
                    print("No hay turno para el día Martes")
        case 2:
            while True:
                dia = input("Eliga el día: Lunes=1 y Martes=2: ")
                if not dia.isdigit():
                    print("Ingrese 1 si quiere cancelar un turno el día Lunes o 2 si quiere cancelar un turno el día Martes")
                    continue
                dia = int(dia)
                if dia not in [1, 2]:
                    print("Ingrese 1 si quiere cancelar un turno el día Lunes o 2 si quiere cancelar un turno el día Martes")
                    continue
                else:
                    break

            while True:
                nombre_paciente = input("Ingresar nombre paciente: ")
                if nombre_paciente.isalpha():
                    break
                else:
                    print("Ingrese un nombre válido")

            if dia == 1:
                if lunes1 == nombre_paciente:
                    lunes1 = "Libre"
                    print(f"Se borro el 1er turno del día Lunes para el paciente {nombre_paciente}")
                elif lunes2 == nombre_paciente:
                    lunes2 = "Libre"
                    print(f"Se borro el 2do turno del día Lunes para el paciente {nombre_paciente}")
                elif lunes3 == nombre_paciente:
                    lunes3 = "Libre"
                    print(f"Se borro el 3er turno del día Lunes para el paciente {nombre_paciente}")
                elif lunes4 == nombre_paciente:
                    lunes4 = "Libre"
                    print(f"Se borro el 4to turno del día Lunes para el paciente {nombre_paciente}")
                else:
                    print(f"El paciente {nombre_paciente} no posee turnos para el día Lunes")
            elif dia == 2:
                if martes1 == nombre_paciente:
                    martes1 = "Libre"
                    print(f"Se borro el 1er turno del día Martes para el paciente {nombre_paciente}")
                elif martes2 == nombre_paciente:
                    martes2 = "Libre"
                    print(f"Se borro el 2do turno del día Martes para el paciente {nombre_paciente}")
                elif martes3 == nombre_paciente:
                    martes3 = "Libre"
                    print(f"Se borro el 3er turno del día Martes para el paciente {nombre_paciente}")
                else:
                    print(f"El paciente {nombre_paciente} no posee turnos para el día Martes")
        case 3:
            while True:
                dia = input("Eliga el día: Lunes=1 y Martes=2: ")
                if not dia.isdigit():
                    print("Ingrese 1 si quiere reservar un turno el día Lunes o 2 si quiere reservar un turno el día Martes")
                    continue
                dia = int(dia)
                if dia not in [1, 2]:
                    print("Ingrese 1 si quiere reservar un turno el día Lunes o 2 si quiere reservar un turno el día Martes")
                    continue
                else:
                    break

            if dia == 1:
                print("Los turnos del día Lunes son: ")
                print(f"Lunes 1er turno: {lunes1}")
                print(f"Lunes 2do turno: {lunes2}")
                print(f"Lunes 3er turno: {lunes3}")
                print(f"Lunes 4to turno: {lunes4}")
            elif dia == 2:
                print("Los turnos del día Martes son: ")
                print(f"Martes 1er turno: {martes1}")
                print(f"Martes 2do turno: {martes2}")
                print(f"Martes 3er turno: {martes3}")
        case 4:
            turnos_lunes = 0
            turnos_martes = 0
            turnos_disponibles_lunes = 0
            turnos_disponibles_martes = 0

            print("----------------LUNES----------------")
            if lunes1 != "Libre":
                turnos_lunes += 1
                print("El 1er turno del Lunes esta ocupado")
            else:
                turnos_disponibles_lunes += 1
                print("El 1er turno del Lunes esta libre")
            if lunes2 != "Libre":
                turnos_lunes += 1
                print("El 2do turno del Lunes esta ocupado")
            else:
                turnos_disponibles_lunes += 1
                print("El 2do turno del Lunes esta libre")
            if lunes3 != "Libre":
                turnos_lunes += 1
                print("El 3er turno del Lunes esta ocupado")
            else:
                turnos_disponibles_lunes += 1
                print("El 3er turno del Lunes esta libre")
            if lunes4 != "Libre":
                turnos_lunes += 1
                print("El 4to turno del Lunes esta ocupado")
            else:
                turnos_disponibles_lunes += 1
                print("El 4to turno del Lunes esta libre")

            print("----------------MARTES----------------")
            if martes1 != "Libre":
                turnos_martes += 1
                print("El 1er turno del Martes esta ocupado")
            else:
                turnos_disponibles_martes += 1
                print("El 1er turno del Martes esta libre")
            if martes2 != "Libre":
                turnos_martes += 1
                print("El 2do turno del Martes esta ocupado")
            else:
                turnos_disponibles_martes += 1
                print("El 2do turno del Martes esta libre")
            if martes3 != "Libre":
                turnos_martes += 1
                print("El 3er turno del Martes esta ocupado")
            else:
                turnos_disponibles_martes += 1
                print("El 3er turno del Martes esta libre")

            print("----------------DÍAS CON MAS TURNOS----------------")
            if turnos_lunes > turnos_martes:
                print("El día con mas turnos es el Lunes")
            elif turnos_martes > turnos_lunes:
                print("El día con mas turnos es el Martes")
            else:
                print(f"Ambos días tiene la misma cantidad de turnos: Lunes -> {turnos_lunes}, Martes -> {turnos_martes}")
        case 5:
            print("Cerrando sesión ...")
            break