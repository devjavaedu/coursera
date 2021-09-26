# import pytest

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

# @pytest.mark.parametrize("entrada, esperado", [
#     (Triangulo(4, 4, 4), 12),
#     (Triangulo(3, 4, 5), 12),
#     (Triangulo(1, 2, 1), 4)
# ])
# def test_tipo_lado(entrada, esperado):
#     assert Triangulo.perimetro(entrada) == esperado