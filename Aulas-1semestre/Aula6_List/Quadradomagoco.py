def quadrado_magico(l):
    linha0 = sum(l[0]) 
    for i in range(len(l)):
        if sum(l[i]) != linha0:
            return False
    for a in range(len(l)):
        somacoluna = 0
        for i in range(len(l)):
            somacoluna += l[i][a]
        if somacoluna != linha0:
            return False
    somadiagonal = 0
    for i in range(len(l)):
        somadiagonal += l[i][i] 
    if somadiagonal != linha0:
        return False
    somadiagonal2 = 0
    for i in range(len(l)):
        somadiagonal2 += l[i][len(l) -1 - i] 
    if somadiagonal2 != linha0:
        return False
    return True

            