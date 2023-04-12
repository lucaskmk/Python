def mais_frequente(lp):
    dt = {}
    l= 0
    for i in lp:
        if i in dt:
            dt[i] += 1
        else:
            dt[i] = 1
    for k, v in dt.items():
        if v == max(dt.values()):
            return k
            break
def mais_frequente(lp):
    lpu = set(lp)
    maxc = 0
    maxw = ''
    for w in lpu:
        c = 0
        for w2 in lp:
            if w2 == w:
                c += 1
        if c > maxc:
            maxc = c
            maxw = w
    return maxw