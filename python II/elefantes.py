def incomodam(numero):
    default = ""
    if numero > 0:
        default = "incomodam "
        return default + incomodam(numero-1)
    return default

def elefantes(numero, maximo=None):

    if maximo is None:
        maximo, numero = numero, 2

    if numero <= maximo:
        if numero == 2:
            frase = "Um elefante incomoda muita gente\n"
            frase += str(numero) + " elefantes " + incomodam(numero) + "muito mais\n"
        else:
            frase = str(numero) + " elefantes " + incomodam(numero) + "muito mais\n"

        if numero < maximo:
            frase += str(numero) + " elefantes incomodam muita gente\n"

        return frase + elefantes(numero + 1, maximo)

    return ""

#print(elefantes(3))