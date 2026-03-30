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