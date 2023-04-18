def dias_de_racao(lrac, dpet):
    maxqtde = 0
    if len(lrac) == 0 :
        return 0
    if dpet['idade'] <= 1:
        dpet['idade'] = 'filhote'
    elif dpet['idade'] > 1 and dpet['idade'] < 8:
        dpet['idade'] = 'adulto'
    elif dpet['idade'] >= 8:
        dpet['idade'] = 'idoso'
    for nestoques in range(len(lrac)):
        if (lrac[nestoques]['indicado'] == dpet['idade']) and (lrac[nestoques]['porte'] == dpet['porte']):
            maxqtde += lrac[nestoques]['qtde']
    return int( (maxqtde*1000) / dpet['gramas_dia']  )