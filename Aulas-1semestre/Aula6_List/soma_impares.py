def soma_impares(lista):
    soma =0
    for numero in lista:
        if numero % 2 == 1:
            soma += numero
    return soma