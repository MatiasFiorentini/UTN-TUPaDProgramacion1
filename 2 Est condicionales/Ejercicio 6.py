consumo_mensual = float(input("Ingrese el consumo mensual de energía eléctrica en kilvatios (kWh): "))

if  0 <= consumo_mensual < 150:
    print("Consumo bajo")
elif 150 <= consumo_mensual <= 300:
    print("Consumo medio")
elif consumo_mensual > 300:
    print("Consumo alto.")
    if consumo_mensual > 500:
        print("Considere medidas de ahorro energético.")