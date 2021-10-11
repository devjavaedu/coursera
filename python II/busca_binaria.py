def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1
    found = False
    while primeiro <= ultimo and not found:
        meio = (primeiro + ultimo) // 2
        print(meio)
        if lista[meio] == elemento:
            found = True
            return meio
        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return found

#print(busca(['a', 'e', 'i'], 'e'))
#print(busca([1, 2, 3, 4, 5], 6))
#print(busca([1, 2, 3, 4, 5, 6], 4))