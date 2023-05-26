def maior_produto3(lista):
    l = [max(lista)]
    lista.remove(max(lista))
    l.append(max(lista))
    lista.remove(max(lista))
    l.append(max(lista))
    calculo = l[0] * l[1] * l[2]
    return calculo


#================================
lista = []
def maior_produto3(lista):
    lista.sort()
    if (lista[0] * lista[1]) > (lista[-1] * lista[-2]):
        return lista[0] * lista[1] * lista[-1]
    else:
        return lista[-1] * lista[-2] * lista[-3]
