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