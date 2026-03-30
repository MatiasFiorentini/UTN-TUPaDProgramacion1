usuario_correcto = "alumno"
clave_correcta = "python123"
contador = 0
acceso_concedido = False

while contador < 3:
    usuario = input("Ingrese un usuario: ")
    contrasenia = input("Ingrese una contraseña: ")

    if usuario == usuario_correcto and contrasenia == clave_correcta:
        print("Acceso concedido")
        acceso_concedido = True
        break
    else:
        print("Credenciales inválidas")
        contador += 1

if acceso_concedido:
    while True:
        print("Menú:")
        print("1) Estado Inscripción 2) Cambiar calve 3) Mensaje 4) Salir")

        while True:
            opcion = input("Seleccione algun número del menú: ")

            if not opcion.isdigit():
                print("Ingrese un valor numérico")
                continue

            opcion = int(opcion)

            if 1 > opcion > 4:
                print("Debe elegir un número del 1 al 4")
                continue

            break

        match opcion:
            case 1:
                print("Inscripto")
            case 2:
                while True:
                    nueva_clave = input("Ingrese una nueva clave (debe tener 6 caracteres o más): ")
                    confirmacion_calve = input("Confirme la clave ingresada: ")
                    if nueva_clave != confirmacion_calve:
                        print("La nueva clave y la confirmación deben coincidir. Por favor ingrese de nuevo las claves")
                    elif len(nueva_clave) < 6:
                        print("La constraseña debe tener como mínimo 6 caracteres")
                    else:
                        print("La nueva contraseña fue guardada")
                        clave_correcta = nueva_clave
                        break
            case 3:
                 print("La constancia vence al talento")
            case 4:
                print("Salida del sistema")
                break