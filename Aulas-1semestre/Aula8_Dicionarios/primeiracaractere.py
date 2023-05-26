def primeiras_ocorrencias(strr):
    d = {}
    for l in range(len(strr)):
        if strr[l] not in d:
            d[strr[l]] = l
    return d