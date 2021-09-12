playlist = ["Um", "Dois", "Três", "Quatro", "Cinco"]
print(len(playlist))
playlist.append("Seis")
print(len(playlist))

flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1


animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]

animais[-3] = "piriquito"
for l in animais:
    print(l)

animais2 = animais[1:4]

print(animais2)

del animais2[0:2]

print(animais2)

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(len(alfabeto))

letras = alfabeto[:]

print(letras)

print(len(alfabeto[13:27]))

letras = alfabeto[1:10]

print(letras)

print(alfabeto[0:13])

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes[:]
carnes2.append("ponta de alcatra")

print(carnes)
print(carnes2)

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
if "ponta de alcatra" in carnes:
    print("XXX")
else:
    if "ponta de alcatra" in carnes2:
        print("YYY")
    else:
        print("ZZZ")

carnes1 = ["picanha", "alcatra"]
carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
carnes3 = carnes2 + carnes1


print(carnes1)
print(carnes2)
print(carnes3)

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
x = carnes
del (x[-1])

print(carnes)
print(x)