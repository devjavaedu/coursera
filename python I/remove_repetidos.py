def remove_repetidos(lista):
    unicos = []
    for x in lista:
        if x not in unicos:
            unicos.append(x)
    return sorted(unicos)