energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

while True:
    agente = input("Ingrese nombre del agente: ")
    if agente.isalpha():
        break
    else:
        print("Error: solo letras")

print(f"Bienvenido agente {agente}")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("Sistema bloqueado por alarma. DERROTA")
        break

    print("")
    print("----- ESTADO -----")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")

    print("")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    while True:
        opcion = input("Elegir opción: ")
        if not opcion.isdigit():
            print("Ingrese un número válido")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 3:
            print("Opción inválida")
            continue

        break

    match opcion:
        case 1:
            energia -= 20
            tiempo -= 2
            racha_forzar += 1

            if racha_forzar == 3:
                print("Forzaste 3 veces seguidas. Se activó la alarma.")
                alarma = True
                continue

            if energia < 40:
                while True:
                    riesgo = input("Riesgo de alarma (1-3): ")
                    if not riesgo.isdigit():
                        print("Número inválido")
                        continue

                    riesgo = int(riesgo)

                    if riesgo < 1 or riesgo > 3:
                        print("Debe ser entre 1 y 3")
                        continue

                    break

                if riesgo == 3:
                    print("Se activó la alarma!")
                    alarma = True
                    continue

            if not alarma:
                cerraduras_abiertas += 1
                print("Abriste una cerradura")

        case 2:
            energia -= 10
            tiempo -= 3
            racha_forzar = 0

            print("Hackeando...")

            for i in range(4):
                codigo_parcial += "A"
                print("Código:", codigo_parcial)

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Cerradura abierta por hackeo")

        case 3:
            energia += 15
            if energia > 100:
                energia = 100

            tiempo -= 1
            racha_forzar = 0

            if alarma:
                energia -= 10
                print("Alarma activa, perdés energía extra")

            print("Descansaste")

print("")
print("----- RESULTADO -----")

if cerraduras_abiertas == 3:
    print("VICTORIA: Abriste la bóveda")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: Te quedaste sin recursos")