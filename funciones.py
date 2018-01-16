
def esPalindromo(cadena):
    rangoIterable = range(0, int(len(cadena)/2))
    rangoCadena = len(cadena) - 1
    palindromo = True

    for posicion in rangoIterable:
        if cadena[posicion] != cadena[rangoCadena - posicion]:
            palindromo = False
            break

    return palindromo

def coincidenciasChar(cadena, charBusqueda):
    coincidencias = 0

    for charCadena in cadena:
        if(charCadena == charBusqueda):
            coincidencias+=1

    return coincidencias

def nucletidosSobrantes(cadena_gen):
    charSobrantes = []
    maxCharPorNucleotidos = int(len(cadena_gen)/4)

    if(cadena_gen.count("A") > maxCharPorNucleotidos ):
        for index in range(0, cadena_gen.count("A") - maxCharPorNucleotidos):
            charSobrantes.append("A")
    if(cadena_gen.count("C") > maxCharPorNucleotidos ):
        for index in range(0, cadena_gen.count("C") - maxCharPorNucleotidos):
            charSobrantes.append("C")
    if(cadena_gen.count("T") > maxCharPorNucleotidos ):
        for index in range(0, cadena_gen.count("T") - maxCharPorNucleotidos):
            charSobrantes.append("T")
    if(cadena_gen.count("G") > maxCharPorNucleotidos ):
        for index in range(0, cadena_gen.count("G") - maxCharPorNucleotidos):
            charSobrantes.append("G")

    return charSobrantes

def contieneSubcadena(cadena_gen, subcadena):
    subcadena = list(subcadena)
    cadena_gen = list(cadena_gen)
    for charGen in cadena_gen:
        for charSubcadena in subcadena:
            if (charGen == charSubcadena):
                subcadena.remove(charSubcadena)
                break

    if subcadena:
        return False
    else:
        return True
