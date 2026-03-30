"""
| Fórmula 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡                 |
| (9/5) * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32 |
"""

grados_celcius = float(input("Ingrese una temperatura en grados Celsius: "))
grados_fahrenheit = (9/5) * grados_celcius + 32

print(f"El equivalente en grados Fahrenheit es {grados_fahrenheit}")