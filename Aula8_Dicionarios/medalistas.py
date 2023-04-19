def mais_medalhas(da):
    dc = {}
    for i in da:
        if i['nacionalidade'] in  dc:
            dc[i['nacionalidade']] += i['ouro']
        else:
            dc[i['nacionalidade']] = i['ouro']
    for j,l in dc.items():
        if l == max(dc.values()):
            return j