#Ejercicio 1
"""
print("Hola mundo")
"""

"""
#Ejercicio 2

nombre = input("Ingrese su nombre: ")
nombre = nombre.capitalize()

print(f"Hola {nombre}")
"""

#Ejercicio 3
"""
nombre = input("Ingrese su nombre: ").capitalize()
apellido = input("Ingrese su apellido: ").capitalize()
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su lugar de residencia/país: ").capitalize()

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")
"""

#Ejercicio 4
"""
| Concepto      | Qué es                        | Fórmula |
| ------------- | ----------------------------- | ------- |
| Radio (r)     | Distancia del centro al borde | —       |
| Perímetro     | Contorno del círculo          | `2πr`   |
| Área**        | Superficie interna            | `πr²`   |
"""

"""
radio = float(input("Ingrese el radio de un círculo: "))
area = 3.14 * (radio**2) 
perimetro = 2 * 3.14 * radio 

print(f"El área del círculo es {area}, y el perímetro es {perimetro}")
"""
"""
import math

radio = float(input("Ingrese el radio de un círculo: "))
area = math.pi * (radio**2)
perimetro = 2 * math.pi * radio

print(f"El área del círculo es {area}, y el perímetro es {perimetro}")
"""

#Ejercicio 5
"""
segundos = int(input("Escriba una cantidad de segundos y se le dirá a cuantas horas equivale: "))

horas = segundos / 3600 # 1 hora = 60 minutos * 60 segundos (cantidad de segundos equivalentes a una hora)

print(f"Usted ingreso {segundos} segundos. Equivalen a {horas} horas")
"""

#Ejercicio 6

"""
numero = int(input("Ingrese un número y se mostrará la tabla de multiplicar de ese número: "))

for i in range(1,11):
    print(f"{numero} * {i} = {numero * i}")
"""

#Ejercicio 7

"""
print("Ingrese dos numero enteros que sean distintos de cero")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 == 0 or numero2 == 0 :
    print("Ha ingresado un numero igual a cero. Intente nuevamente")
else :
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    print(f"La suma de los número es {suma}")
    print(f"la resta de los números es {resta}")
    print(f"la multiplicación de los números es {multiplicacion}")
    print(f"la división de los números es {division}")
"""

#Ejercicio 8
"""
| Fórmula IMC                |
| 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / 𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚**2 |
"""
"""
print("Ingrese su altura y peso para luego calcular su Índice de masa corporal")
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = round(peso / (altura**2),2)

print(f"Su IMC es igual a {imc}")
"""

#Ejercicio 9
"""
| Fórmula 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡                 |
| (9/5) * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32 |
"""

"""
grados_celcius = float(input("Ingrese una temperatura en grados Celsius: "))
grados_fahrenheit = (9/5) * grados_celcius + 32

print(f"El equivalente en grados Fahrenheit es {grados_fahrenheit}")
"""

"""
#Ejercicio 10

print("Ingrese 3 numero para luego calcular el promedio de dichos numeros")
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio es {promedio}")

#Otra forma de clacular el promedio
import statistics
promedio = statistics.mean([numero1, numero2, numero3])
print(f"El promedio es {promedio}")
"""

