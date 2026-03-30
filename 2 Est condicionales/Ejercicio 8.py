nombre = input("Ingrese su nombre: ")
opcion = int(input("Ahora seleccione alguna de las opciones:\n"
                   "1- Si quiere su nombre en mayúsculas\n"
                   "2- Si quiere su nombre en minúsculas\n"
                   "3- Si quiere su nombre con la primera letra mayúscula\n"))

if  opcion == 1:
    print(f"{nombre.upper()}")
elif opcion == 2:
    print(f"{nombre.lower()}")
elif opcion == 3:
    print(f"{nombre.title()}")
else:
    print("Ingrese una opcion válida")