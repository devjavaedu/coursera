#import pytest

def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])

#@pytest.mark.parametrize("entrada, esperado", [
#    ([1,1,1,1,1],5),
#    ([1,2,3,4,5],15),
#    ([1,3,5,7,9],25),
#    ([2,4,6,8,10],30),
#    ([-10, 0, 10], 0)
#])
#def test_soma_lista(entrada, esperado):
#    assert soma_lista(entrada) == esperado