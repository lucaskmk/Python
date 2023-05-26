#def subtracao_de_listas(lista1, lista2):
#    return [x for x in lista1 if x not in lista2]
def subtracao_de_listas(lista1, lista2):
    l = []
    for x in lista1:
        if x not in lista2:
            l += [x]
    return l




