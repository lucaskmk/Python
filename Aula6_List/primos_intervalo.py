def eh_primo(m):
    j = 0
    if m < 0:
        return False
    if m == 2:
        return True
    if m == 1 or m == 0:
        return False
    for count in range(2, m):
        if (m%count == 0):
            j += 1
    if j == 0:
        return True
    else:
        return False
#===============================================
def primos_entre(a, b):
    lista = []
    j = a
    while j <= b:
        if eh_primo(j) == True:
            lista.append(j)
        j += 1
    return lista
print(primos_entre(4, 5))