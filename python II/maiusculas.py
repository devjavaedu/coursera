def maiusculas(frase):
    resultado = ""
    indice = 0
    while indice < len(frase):
        value = ord(frase[indice])
        if value == ord(frase[indice].upper()) and (65 <= value <= 90) :
            resultado = resultado + frase[indice].strip()
        indice += 1
    return resultado