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

diccionarioPalabras =  {
      "0": { "unidad": "0"},
      "1": { "unidad": "uno", "decena": "dieci", "centena": "ciento"},
      "2": { "unidad": "dos", "decena": "veinti", "centena": "doscientos"},
      "3": { "unidad": "tres", "decena": "treinta", "centena": "trescientos"},
      "4": { "unidad": "cuatro", "decena": "cuarenta", "centena": "cuatrocientos"},
      "5": { "unidad": "cinco", "decena": "cincuenta", "centena": "quinientos"},
      "6": { "unidad": "seis", "decena": "sesenta", "centena": "seiscientos"},
      "7": { "unidad": "siete", "decena": "setenta", "centena": "setecientos"},
      "8": { "unidad": "ocho", "decena": "ochenta", "centena": "ochocientos"},
      "9": { "unidad": "nueve", "decena": "noventa", "centena": "novecientos"},
      "excepciones": {
          "10": "diez",
          "11": "once",
          "12": "doce",
          "13": "trece",
          "14": "catorce",
          "15": "quince",
          "20": "veinte",
         }
      }

cadena = input("3. Introduce el numero: ")


if int(cadena) >= 0 and int(cadena) <= 1000:

    if len(cadena) == 1:
        if cadena == "0":
            print("cero")
        else:
            print(diccionarioPalabras[cadena]["unidad"])

    if len(cadena) == 2:
        if (int(cadena) >= 10 and int(cadena) <= 15) or int(cadena) == 20:
            print(diccionarioPalabras["excepciones"][cadena])
        elif int(cadena) >= 16 and int(cadena) <= 29:
            print(diccionarioPalabras[cadena[0]]["decena"] + diccionarioPalabras[cadena[1]]["unidad"])
        else:
            if cadena[1] == "0":
                print(diccionarioPalabras[cadena[0]]["decena"])
            else :
                print(diccionarioPalabras[cadena[0]]["decena"] + " y " + diccionarioPalabras[cadena[1]]["unidad"])

    if len(cadena) == 3:
        if cadena == "100":
            print("cien")
        else:
            if (int(cadena[1:]) >= 10 and int(cadena[1:]) <= 15) or int(cadena[1:]) == 20:
                print(diccionarioPalabras[cadena[0]]["centena"] + " " + diccionarioPalabras["excepciones"][cadena[1:]])
            elif int(cadena[1:]) >= 16 and int(cadena[1:]) <= 29:
                print(diccionarioPalabras[cadena[0]]["centena"] + " " + diccionarioPalabras[cadena[1]]["decena"] + diccionarioPalabras[cadena[2]]["unidad"])
            else:
                if cadena[1:] == "00":
                    print( diccionarioPalabras[cadena[0]]["centena"])
                if cadena[2] == "0":
                    print( diccionarioPalabras[cadena[0]]["centena"] + " " + diccionarioPalabras[cadena[1]]["decena"])
                else:
                    print( diccionarioPalabras[cadena[0]]["centena"] + " " + diccionarioPalabras[cadena[1]]["decena"] + " y " + diccionarioPalabras[cadena[2]]["unidad"])
    else:
        print("mil")

cadena = input("4. Introduce el string: ")

listaNucleotidosSobrantes = nucletidosSobrantes(cadena)
largoSubcadena = len(listaNucleotidosSobrantes)
largostringGen = len(cadena)
control = True
print(listaNucleotidosSobrantes)

if largoSubcadena == 0:
    print("0")
else:
    while control:
        for iteracion in range( (largostringGen - largoSubcadena) + 1 ):

            if contieneSubcadena(cadena[iteracion:iteracion+largoSubcadena], listaNucleotidosSobrantes):
                print(largoSubcadena)
                control = False
                break

        largoSubcadena += 1
