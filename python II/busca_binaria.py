import pytest

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

@pytest.mark.parametrize("lista, valor, esperado", [
    (['a', 'e', 'i'], 'e', 1),
    ([1, 2, 3, 4, 5], 6, False),
    ([1, 2, 3, 4, 5, 6], 4, 3)
])
def test_busca(lista, valor, esperado):
    assert busca(lista, valor) == esperado

def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1
    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1, max)
    else:
        return meio

a = [10,20,30,40,50,60]
@pytest.mark.parametrize("lista, valor, esperado", [
    (a, 0, False),
    (a, 10, 0),
    (a, 20, 1),
    (a, 30, 2),
    (a, 40, 3),
    (a, 50, 4),
    (a, 60, 5),
    (a, 70, False),
])
def test_busca_binaria(lista, valor, esperado):
    assert busca_binaria(lista, valor) == esperado