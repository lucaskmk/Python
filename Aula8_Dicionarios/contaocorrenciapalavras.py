def conta_ocorrencias(l1):
    co = {}
    for palavras in range(len(l1)):
        if l1[palavras] in co:
            co[l1[palavras]] += 1
        else:
            co[l1[palavras]] = 1
    return co