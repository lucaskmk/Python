lista = [1, 2, 4, 7, 3, 9, 3, 3]
def estritamente_crescente_(lista):
    for numero in lista:
        if lista[numero] == [set(lista)]:
            del lista[numero]
    return lista.sort()

def estritamente_crescente(lista):
    lista = list(dict.fromkeys(lista))
    lista.sort()
    return lista

print(estritamente_crescente(lista))

lista = [3, 1, 3, 2, 3, 5, 4, 6 ]
def estritamente_crescente(lista):
    lista = list(dict.fromkeys(lista))
    for i in range(len(lista)):
        if i < lista[0]:
            del lista[i]
    lista.sort()
    return lista
print(estritamente_crescente(lista))