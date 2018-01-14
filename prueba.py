
cadena = input("Introduce una cadena de texto: ")

rangoIterable = range(0, int(len(cadena)/2))
rangocadena = len(cadena) - 1
esPalindromo = True

for posicion in rangoIterable:
    if cadena[posicion] != cadena[rangocadena - posicion]:
        print("entro")
        esPalindromo = False
        break



if esPalindromo:
    print("Es palindromo")
else:
    print("No es palindromo")
