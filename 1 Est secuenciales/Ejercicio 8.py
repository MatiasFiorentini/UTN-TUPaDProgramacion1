"""
| Fórmula IMC                |
| 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / 𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚**2 |
"""

print("Ingrese su altura y peso para luego calcular su Índice de masa corporal")
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = round(peso / (altura**2),2)

print(f"Su IMC es igual a {imc}")