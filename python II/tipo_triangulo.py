# import pytest

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if (self.a == self.b and self.a == self.c):
            return 'equilátero'
        else:
            if(self.a == self.b or self.a == self.c or self.b == self.c):
                return 'isósceles'
            else:
                if(self.a != self.b and self.b != self.c and self.a != self.c):
                    return 'escaleno'


# @pytest.mark.parametrize("entrada, esperado", [
#     (Triangulo(4, 4, 4), 'equilátero'),
#     (Triangulo(3, 4, 5), 'escaleno'),
#     (Triangulo(1, 2, 1), 'isósceles')
# ])
# def test_tipo_lado(entrada, esperado):
#     assert Triangulo.tipo_lado(entrada) == esperado