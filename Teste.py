frota = {
  "navio-tanque":[
    [[6,1],[6,2],[6,3]]
  ]
}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3
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
        frota[nome_navio] = l
    return frota


print(preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho))    