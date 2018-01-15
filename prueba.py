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

cadena = list(cadena)

esReducible = len(cadena) != len(set(cadena))

while(esReducible):

    cosa = cadena[0]

    coincidencias = coincidenciasChar(cadena, cosa)

    if(coincidencias % 2 == 0):
        for indice in range(coincidencias):
            cadena.remove(cosa)
    if(coincidencias % 2 == 1 ):
        for indice in range(coincidencias - 1):
            cadena.remove(cosa)

    esReducible = len(cadena) != len(set(cadena))

print(cadena)
