def interseccao_valores(di1,di2):
    l = []
    for val in di1.values():
        for same in di2.values():
            if val == same:
                l.append(val)
    return l