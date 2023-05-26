def nomes_com_vogais(nomes):
    vog = ['A', 'E', 'I', 'O' , 'U']
    totaldevog = [0, 0]
    for nome in nomes:
        if nome[0] in vog:
            totaldevog[0] += 1
        else:
            totaldevog[1] += 1
    return totaldevog