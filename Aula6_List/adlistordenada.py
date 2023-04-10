def adiciona_em_ordem(p,d,l):
    l1 = []
    while len(l1) <= len(l):
        for i in l:
            if i[1] < d:
                l1.append(i)
        l1.append([p,d])
        for j in l:
            if j[1] > d:
                l1.append(j)
    return l1
