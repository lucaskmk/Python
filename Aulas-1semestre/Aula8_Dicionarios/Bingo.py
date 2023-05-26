def define_vencedores(ns, dps):
    dt = {}
    returnl = []
    for nome, lnums in dps.items():
        for num in lnums:
            if num in ns:
                if nome not in dt:
                    dt[nome] = 1
                else:
                    dt[nome] += 1
    maxnums = 0
    for nome2, val in dt.items():
        if val > maxnums:
            maxnums = val
    if maxnums == 0:
        returnl = [x for x in dps.keys()]
    else:
        for nome2 , val in dt.items():
            if val == maxnums:
                returnl += [nome2]
    return returnl