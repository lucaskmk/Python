def calcula_norma(lista):
    soma = 0
    for i in range(len(lista)):
        i = (lista[i])**2
        soma+=i
    return abs(soma** 0.5 )