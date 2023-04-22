def define_posicoes(linha, coluna, orientacao, tamanho):
    l = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            l.append([(linha+i), coluna])
        if orientacao == 'horizontal':
            l.append([linha, (coluna+i)])
    return l
#=============================================================================================
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    l = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            l.append([(linha+i), coluna])
        if orientacao == 'horizontal':
            l.append([linha, (coluna+i)])
    if nome_navio in frota.keys():
        frota[nome_navio] += [l]
    else:
        frota[nome_navio] = [l]
    return frota
#=============================================================================================
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
#=============================================================================================
def posiciona_frota(frota):
    l = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(10):
        l[i] += [0 for x in range(10)]
    for barco, cordenadas_geral in frota.items():
        for cordenada_umbarco in cordenadas_geral:
            for posicao in cordenada_umbarco:
                for T in range(10):
                    for j in range(10):
                        if [T,j] == [posicao[0],posicao[1]]:
                            l[T][j] = 1
    return l
#=============================================================================================
def afundados(frota, tabuleiro):
    total_afundados = 0
    for barco, cordenadas_geral in frota.items():
        for cordenada_umbarco in cordenadas_geral:
            afundo = 0
            for posicao in cordenada_umbarco:
                if tabuleiro[posicao[0]][posicao[1]] == 'X':
                    afundo += 1
                if afundo == len(cordenada_umbarco):
                    total_afundados += 1
    return total_afundados
#=============================================================================================
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    validacao = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            validacao.append([(linha+i), coluna])
            if (linha+i) > 9:
                return False
        if orientacao == 'horizontal':
            validacao.append([linha, (coluna+i)])
            if (coluna+i) > 9:
                return False
    for barco, cordenadas_geral in frota.items():
        for cordenada_umbarco in cordenadas_geral:
            for posicao in cordenada_umbarco:
                for itemvalido in validacao:
                    if itemvalido == [posicao[0],posicao[1]]:
                        return False
    return True