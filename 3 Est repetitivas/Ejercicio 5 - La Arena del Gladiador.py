print("--- BIENVENIDO A LA ARENA ---")
print(" ")

while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras.")


vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_jugador = True

print("=== INICIO DEL COMBATE ===")


while vida_jugador > 0 and vida_enemigo > 0:

    print(" ")
    print("=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")


    while True:
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 3:
            print("Error: Opción inválida.")
            continue

        break


    match opcion:
        case 1:
            if vida_enemigo < 20:
                danio = danio_pesado * 1.5
                print("¡Golpe crítico!")
            else:
                danio = danio_pesado

            vida_enemigo -= danio
            print(f"¡Atacaste al enemigo por {danio} de daño!")

        case 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        case 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Te curaste 30 puntos de vida")
            else:
                print("¡No quedan pociones!")


    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo te atacó por {danio_enemigo} puntos!")


print(" ")
print("=== FIN DEL JUEGO ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")