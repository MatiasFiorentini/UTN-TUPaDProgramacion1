frase = input("Ingrese una frase o palabara: ")

if  frase[-1].lower() in "aeiou":
    print(f"{frase}!")
else:
    print(frase)