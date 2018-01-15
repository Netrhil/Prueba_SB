from funciones import *

cadena = input("1. Introduce una cadena de texto: ")

iteraciones = range(len(cadena))

Resultado = -1

if esPalindromo(cadena):
    Resultado = 0
else:
    for posicion in iteraciones:
        cadenaSinCaracter = cadena[:posicion] + cadena[posicion + 1:]
        if esPalindromo(cadenaSinCaracter):
            Resultado = posicion + 1
            break

print(Resultado)

cadena = input("2. Introduce una cadena de texto: ")
