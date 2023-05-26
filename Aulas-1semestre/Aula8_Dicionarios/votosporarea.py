def apura_area(lvps, dcpp):
    dregiao = {}
    for secao in lvps:
        dt = {}
        for candidato,votos in secao['candidatos'].items() :
            if candidato in ['nulos','brancos']:
                if candidato not in dt:
                    dt[candidato] = votos
                else:
                    dt[candidato] += votos  
            else:
                for partidos, listacandidato in dcpp.items():
                    if candidato in listacandidato:
                        if partidos not in dt:
                            dt[partidos] = votos
                        else:
                            dt[partidos] += votos 

        if secao['area'] not in dregiao:
            dregiao[secao['area']] = dt
        else:
            for it in dt:
                if it not in dregiao[secao['area']]:
                    dregiao[secao['area']][it] = dt[it]
                else:
                    dregiao[secao['area']][it] += dt[it]
    return dregiao