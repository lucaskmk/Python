def calcula_serie(a, b, n):
    i = 0
    soma = 0
    while i < n:
        soma += 1 / ( a ** ( (i)*b) ) 
        i += 1
    return soma