# import pytest

def encontra_impares(lista):
    impares = []
    if len(lista) > 0:
        if lista[0] % 2 != 0:
            impares.append(lista[0])
        impares.extend(encontra_impares(lista[1:]))
    return impares

# @pytest.mark.parametrize("entrada, esperado", [
#    ([1,9, 12, 18, 17],[1,9,17]),
#    ([1,2,3,4,5],[1,3,5]),
#    ([1,3,5,7,9],[1,3,5,7,9]),
#    ([2,4,6,8,10],[]),
#    ([-10, 0, 1, 10], [1])
# ])
# def test_encontra_impares(entrada, esperado):
#    assert encontra_impares(entrada) == esperado