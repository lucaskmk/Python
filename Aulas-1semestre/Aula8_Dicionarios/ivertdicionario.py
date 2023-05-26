def inverte_dicionario(d1):
    nd ={}
    for ke, va in d1.items():
        if va in nd.keys():
            nd[va] += [ke]
        else:
            nd[va] = [ke]
    return nd