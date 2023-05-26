def contabiliza(dic):
    doacoestotal = {}
    for doacoes in dic.values():
        for iten in doacoes:
            lcoisas = iten.split(' ')
            quantidade = int(lcoisas[0])
            coisas = ' '.join(lcoisas[1:-1])
            coisas += ' ' + lcoisas[-1]
            coisas = coisas.strip()
            if coisas in doacoestotal:
                doacoestotal[coisas] += quantidade
            else: 
                doacoestotal[coisas] = quantidade
    return doacoestotal