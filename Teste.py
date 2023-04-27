frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    l = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            l.append([(linha+i), coluna])
        if orientacao == 'horizontal':
            l.append([linha, (coluna+i)])
    if navio in frota.keys():
        frota[navio] += [l]
    else:
        frota[navio] = [l]
    return frota
#================================================================    
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
#================================================================
def pergunta(navio, tamanho):
    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, tamanho))
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if navio == "submarino":
        orientacao = 'vertical'
    else:
        orientacao = int(input('[1] Vertical [2] Horizontal >'))
    if orientacao == 1:
        orientacao = 'vertical'
    elif orientacao == 2:
        orientacao = 'horizontal'
# se for invalido
    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
        return pergunta(navio, tamanho)
# se for valida ja adiciona
    else:
        preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)
        return ''
        
#================================================================
tamanho = ''
for navio in frota:
    if navio == "porta-aviões":
        tamanho = 4
        pergunta(navio, tamanho)

    if navio == "navio-tanque":
        tamanho = 3
        for i in range(2):
            pergunta(navio, tamanho)

    if navio == "contratorpedeiro":
        tamanho = 2
        for i in range(3):
            pergunta(navio, tamanho)

    if navio == "submarino":
        tamanho = 1
        for i in range(4):
            pergunta(navio, tamanho)
print(frota)


#==========================================




def faz_jogada(tabuleiro, linha, coluna):
    xtotal = 0
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
        xtotal+=1
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(frota):
    tabuleiro = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(10):
        tabuleiro[i] += [0 for x in range(10)]
    for barco, cordenadas_geral in frota.items():
        for cordenada_umbarco in cordenadas_geral:
            for posicao in cordenada_umbarco:
                for T in range(10):
                    for j in range(10):
                        if [T,j] == [posicao[0],posicao[1]]:
                            tabuleiro[T][j] = 1
    return tabuleiro
    
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
#==============================================================
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
#==============================================================
jogando = True
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
lposições = []
while jogando:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'
        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto
    #==============================
    monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    linha = int(input('informe um número entre 0 e 9.'))
    while linha not in range(10):
        print('Linha inválida!')
        linha = int(input('informe um número entre 0 e 9.'))
    coluna = int(input('informe um número entre 0 e 9.'))
    while coluna not in range(10):
        print('Coluna inválida!')
        coluna = int(input('informe um número entre 0 e 9.'))
    if [linha, coluna] not in lposições:
        lposições.append([linha, coluna])
        faz_jogada(tabuleiro, linha, coluna)
    else:
        print('A posição linha LINHA e coluna COLUNA já foi informada anteriormente!')
    faz_jogada(tabuleiro, linha, coluna)
    if xtotal == 20:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando == False
    
