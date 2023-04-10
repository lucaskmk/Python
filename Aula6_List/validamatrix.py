def eh_identidade(lista):
    for i in range(len(lista)):
        if (lista[i][i] != 1) or (sum(lista[i]) != 1) or (len(lista) != len(lista[0])):
            return False
    return True
        