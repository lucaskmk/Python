def inverte_lista(lista):
    lista2 = []
    s = len(lista)
    for i in range(s):
        lista2 += [lista[s - i - 1]]
    return lista2