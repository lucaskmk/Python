def interseccao_chaves(di1, di2):
    l = []
    for key in di1:
        for same in di2:
            if key == same:
                l.append(key)
    return l