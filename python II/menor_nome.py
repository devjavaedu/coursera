def menor_nome(nomes):
    smaller = ""
    i = 0
    for item in nomes:
        if ((smaller == "") or (len(item.strip()) < len(smaller))):
            smaller = item.strip()
        i += 1
    smaller = smaller.lower()
    return smaller.capitalize()