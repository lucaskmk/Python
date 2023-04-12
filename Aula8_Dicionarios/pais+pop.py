def mais_populoso(br):
    maxpop = 0
    maxestado = ''
    for estado in br.keys():
        totestado = 0
        for mun, populacao in br[estado].items():
            totestado += populacao
        if totestado > maxpop:
            maxpop = totestado
            maxestado = estado
    return(maxestado)