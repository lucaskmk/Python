def eh_simetrica(matriz):
    if len(matriz) != len(matriz[0]):
        return False
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
    
    return True