# Ejercicio 1
"""
edad = int(input("Ingrese su edad: "))
if edad >= 18 :
    print("Es es mayor de edad")
"""

# Ejercicio 2
"""
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
"""

# Ejercicio 3
"""
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
"""

# Ejercicio 4
"""
edad = int(input("Ingrese su edad: "))
if 0 <= edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
"""

# Ejercicio 5
"""
contrasena = input("Ingrese una contaseña de entre 8 y 14 caracteres: ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
"""

# Ejercicio 6
"""
consumo_mensual = float(input("Ingrese el consumo mensual de energía eléctrica en kilvatios (kWh): "))

if  0 <= consumo_mensual < 150:
    print("Consumo bajo")
elif 150 <= consumo_mensual <= 300:
    print("Consumo medio")
elif consumo_mensual > 300:
    print("Consumo alto.")
    if consumo_mensual > 500:
        print("Considere medidas de ahorro energético.")
"""

# Ejercicio 7
"""
frase = input("Ingrese una frase o palabara: ")

if  frase[-1].lower() in "aeiou":
    print(f"{frase}!")
else:
    print(frase)
"""

# Ejercicio 8
"""
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

match opcion:
    case 1:
        print(f"{nombre.upper()}")
    case 2:
        print(f"{nombre.lower()}")
    case 3:
        print(f"{nombre.title()}")
    case _:
        print("Ingrese una opción valida")
"""

# Ejercicio 9
"""
magnitud_terremoto = float(input("Ingrese la magnitud de un terremoto y luego lo clasificaremos según la escala de Richter: "))

if  magnitud_terremoto < 3:
    print("Muy leve")
elif magnitud_terremoto < 4:
    print("Leve")
elif magnitud_terremoto < 5:
    print("Moderado")
elif magnitud_terremoto < 6:
    print("Fuerte")
elif magnitud_terremoto < 7:
    print("Muy Fuerte")
else:
    print("Extremo")
"""

# Ejercicio 10
"""
hemisferio = int(input("Ingrese en cuál hemisferio se encuenta \n"
                       "1-Norte \n"
                       "2-Sur \n"))

mes_anio = input("Ingrese el mes del año: ").lower()
dia_mes = int(input("Ingrese el día del mes: "))

match hemisferio:
    case 1:
        if mes_anio == "diciembre" and (21 <= dia_mes <= 31):
            print("Usted se encuentra el Invierno")
        elif mes_anio == "enero" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Invierno")
        elif mes_anio == "febrero" and (1 <= dia_mes <= 28):
            print("Usted se encuentra el Invierno")
        elif mes_anio == "marzo" and (1 <= dia_mes <= 20):
            print("Usted se encuentra el Invierno")
        elif mes_anio == "marzo" and (21 <= dia_mes <= 31):
            print("Usted se encuentra el Primavera")
        elif mes_anio == "abril" and (1 <= dia_mes <= 30):
            print("Usted se encuentra el Primavera")
        elif mes_anio == "mayo" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Primavera")
        elif mes_anio == "junio" and (1 <= dia_mes <= 20):
            print("Usted se encuentra el Primavera")
        elif mes_anio == "junio" and (21 <= dia_mes <= 30):
            print("Usted se encuentra el Verano")
        elif mes_anio == "julio" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Verano")
        elif mes_anio == "agosto" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Verano")
        elif mes_anio == "septiembre" and (1 <= dia_mes <= 20):
            print("Usted se encuentra el Verano")
        elif mes_anio == "septiembre" and (21 <= dia_mes <= 30):
            print("Usted se encuentra el Otoño")
        elif mes_anio == "octubre" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Otoño")
        elif mes_anio == "noviembre" and (1 <= dia_mes <= 30):
            print("Usted se encuentra el Otoño")
        elif mes_anio == "diciembre" and (1 <= dia_mes <= 20):
            print("Usted se encuentra el Otoño")
    case 2:
        if mes_anio == "diciembre" and (21 <= dia_mes <= 31):
            print("Usted se encuentra el Verano")
        elif mes_anio == "enero" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Verano")
        elif mes_anio == "febrero" and (1 <= dia_mes <= 28):
            print("Usted se encuentra el Verano")
        elif mes_anio == "marzo" and (1 <= dia_mes <= 20):
            print("Usted se encuentra el Verano")
        elif mes_anio == "marzo" and (21 <= dia_mes <= 31):
            print("Usted se encuentra el Otoño")
        elif mes_anio == "abril" and (1 <= dia_mes <= 30):
            print("Usted se encuentra el Otoño")
        elif mes_anio == "mayo" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Otoño")
        elif mes_anio == "junio" and (1 <= dia_mes <= 20):
            print("Usted se encuentra el Otoño")
        elif mes_anio == "junio" and (21 <= dia_mes <= 30):
            print("Usted se encuentra el Invierno")
        elif mes_anio == "julio" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Invierno")
        elif mes_anio == "agosto" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Invierno")
        elif mes_anio == "septiembre" and (1 <= dia_mes <= 20):
            print("Usted se encuentra el Invierno")
        elif mes_anio == "septiembre" and (21 <= dia_mes <= 30):
            print("Usted se encuentra el Primavera")
        elif mes_anio == "octubre" and (1 <= dia_mes <= 31):
            print("Usted se encuentra el Primavera")
        elif mes_anio == "noviembre" and (1 <= dia_mes <= 30):
            print("Usted se encuentra el Primavera")
        elif mes_anio == "diciembre" and (1 <= dia_mes <= 20):
            print("Usted se encuentra el Primavera")
"""