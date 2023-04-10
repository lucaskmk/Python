def eh_identidade(lista):
    l = len(lista) - 1
    for row in range(len(lista)):
        soma = 0
        for elem in range(len(lista[row])):
            soma += lista[row][elem] * 2 ** (l - elem)
        if soma != 2 ** (l - row):
            return False
    return True

print(eh_identidade([[1,0],[0,1]]))