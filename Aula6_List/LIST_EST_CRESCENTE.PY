def estritamente_crescente(lista):
    # sorted(list(set(lista))) -> <> .sort() -> só para strings
    lista2 = []
    for i in lista:
        if len(lista2) == 0:
            lista2 += [i]
        elif i > max(lista2):
            lista2 += [i]
    return lista2