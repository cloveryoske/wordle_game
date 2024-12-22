from termcolor import colored
import random

with open("palabras.txt", "r", encoding="utf-8") as archivo:
    palabras_5_letras = [palabra.strip() for palabra in archivo.readlines() if len(palabra.strip()) == 5]

def funcionCompararPalabras(adivinar, usuario):
    arrayCopia = list(adivinar)
    arrayUser= list(usuario)
    if adivinar == usuario:
        print(colored(adivinar, "green"))
        print("has acertado!")
        exit(0)
    else:
        for i, char in enumerate(usuario):
                if char == adivinar[i]:
                    print(colored(char, "green"), end=" ")
                    arrayCopia[i] = 0
                elif char in adivinar and char in arrayCopia:
                    if arrayCopia.index(char) == adivinar.index(char) and arrayCopia.count(char) < arrayUser.count(char):
                        arrayUser[i] = 0
                        print(colored(char, "grey"), end=" ")
                    else:
                        indice = arrayCopia.index(char)
                        arrayCopia[indice] = 1
                        print(colored(char, "yellow"), end=" ")
                elif char not in arrayCopia:
                    print(colored(char, "grey"), end=" ")
        print("\n")
palabraAdivinar = random.choice(palabras_5_letras)
print(palabraAdivinar)
intentos= 5
print("introduce una palabra de 5 letras")
while intentos > 0:
    print(f"tienes {intentos} intentos")
    palabraUsuario = input().lower()
    if len(palabraUsuario) != 5:
        print("error tienes que introducir una palabra de 5 letras")
    else:
        funcionCompararPalabras(palabraAdivinar, palabraUsuario)
        intentos = intentos - 1
print(f"oh no! no tienes mas intentos! la palabra era {palabraAdivinar}")
