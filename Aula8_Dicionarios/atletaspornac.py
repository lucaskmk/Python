def agrupa_por_nacionalidade(d):
    r = {}
    for nomeA, nac in d.items():
        nacional = nac["nacionalidade"]
        if nacional not in r:
            r[nacional] = []
        r[nacional].append(nomeA)
    return r