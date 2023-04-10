def numero_no_indice(l):
    a =[]
    for i in range(len(l)):
        if i == l[i]:
            a.append(i)
    return a 