largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

l = 1
a = 1

linha = ""
while a <= altura:
    while l <= largura:
        print("#", end="")
        l = l + 1
    print()
    l = 1
    a = a + 1