import math
def eh_primo(n):
    if n == 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    i = 1
    while 2 * i + 1 <= math.sqrt(n):
        if n % (2 * i + 1) == 0:
            return(False)
        i += 1
    return True
#===============================================
def lista_primos(n):
    lista = []
    m=0
    while len(lista) < n:
        m += 1
        if eh_primo(m) == True:
            lista.append(m)
    return lista

print(lista_primos(1000))