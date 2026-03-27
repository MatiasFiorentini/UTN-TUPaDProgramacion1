while True:
    nombre_cliente = input("Ingrese su nombre: ")
    if nombre_cliente.isalpha():
        break
    else:
        print("Por favor ingrese un nómbre válido")

while True:
    productos = input("Ingrese la cantidad de productos a comprar: ")
    if not productos.isdigit():
        print("Ingrese un valor númerico")
    else:
        productos = int(productos)
        if productos <= 0:
            print("Ingrese un valor númerico mayor a 0")
        else:
            break

total_sin_descuento = 0
total_con_descuento   = 0
precio_final = 0
ahorro = 0
promedio = 0
lista_productos = []

for i in range(1,productos+1):
    while True:
        precio = input(f"Ingrese el precio del prducto n° {i}: ")
        if not precio.isdigit():
            print("Ingrese un precio valido")
        else:
            precio = int(precio)
            if precio <= 0:
                print("Ingrese un valor númerico mayor a 0")
            else:
                break

    while True:
        descuento = input(f"¿El prodcuto n° {i} tiene descunto?: S/N: ").lower()
        if descuento not in ["s", "n"]:
            print("Ingrese S (sí tiene descuento) o N (no tiene descuento)")
        else:
            break

    total_sin_descuento += precio

    if descuento == "s":
        precio_final = precio * 0.9
    else:
        precio_final = precio

    total_con_descuento += precio_final
    lista_productos.append((i,precio,descuento)) #uso una lista para guardar cada prodcuto recorrido + precio + descuento
    ahorro = total_sin_descuento - total_con_descuento

promedio = total_con_descuento / productos


print(f"\nCliente: {nombre_cliente}")
print(f"Cantidad de productos: {productos}")

for prod in lista_productos:
    print(f"Producto {prod[0]} - Precio: {prod[1]} - Descuento: {prod[2]}")

print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

