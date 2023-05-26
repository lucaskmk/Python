def predizer_lingua(linguas, frase):
    crt_est = ['!', '?', ',', ';', '.', ':', ')', '}', ']', '(', '[', '{']
    for crt in crt_est:
        frase = frase.replace(crt, ' ')
    while frase.count('  ') > 0:
        frase = frase.replace('  ', ' ')

    frase = frase.strip()
    frase = frase.lower()
    lpalavras = frase.split(' ')

    print(frase, lpalavras, len(lpalavras))
    dici_pl_origem = {}
    for regioes in linguas:
        dici_pl_origem[regioes] = 0.0
    for lingua, palavras in linguas.items():
        for palavra in lpalavras:
            if palavra.lower() in palavras:
                dici_pl_origem[lingua] += (1.0/len(lpalavras))
    maxv = -1
    maxk = -1
    for k, v in dici_pl_origem.items():
        if v == maxv:
            dici_pl_origem['palpite'] = 'DESCONHECIDA'
            return dici_pl_origem
            break
        elif v == max(dici_pl_origem.values()):
            maxv = v
            maxk = k

    dici_pl_origem['palpite'] = maxk
    return dici_pl_origem


