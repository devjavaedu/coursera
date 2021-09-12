def maior_primo(n):
    out = list()
    lista = [True] * (n + 1)
    last = 0
    for p in range(2, n + 1):
        if (lista[p]):
            out.append(p)
            last = p
            for i in range(p, n + 1, p):
                lista[i] = False
    return last
