def concentracao_nociva(ar):
    nocivos = {}
    ar_proc = {}
    total = 0
    for camada in ar:
        for linha in camada:
            for el in linha:
                total += 1
                if el in ar_proc.keys():
                    ar_proc[el] += 1
                else:
                    ar_proc[el] = 1
    for el in ar_proc.keys():
        ar_proc[el] /= total
        ar_proc[el] *= 100

    for el in ar_proc.keys():
        if el == 'O':
            if ar_proc['O'] < 20:
                nocivos['O'] = ar_proc['O']
        elif el == 'N' :
            if ar_proc['N'] > 70:
                nocivos['N'] = ar_proc['N']
        else:
            if ar_proc[el] > 2:
                nocivos[el] = ar_proc[el]
    if 'O' not in ar_proc.keys():
        nocivos['O'] = 0

    return nocivos