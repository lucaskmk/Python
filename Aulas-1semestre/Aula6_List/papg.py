def verifica_progressaoD(l):
    pa = 0
    pg = 0
    for i in range(2, len(l)):
        if l[i-2] == l[i-1]:
            return 'AG'
        if l[i] or l[i-1] or l[i-2]  == 0:
            return 'NA'
        testePG = l[i-1] / l[i-2]
        if l[i] == l[i-1] * testePG:
            pg += 1
        testePA = l[i-1] - l[i-2]
        if l[i] == l[i-1] + testePA:
            pa +=1
    if pa == (len(l)-2):
        return 'PA'
    if pg == (len(l)-2):
        return 'PG'
    else:
        return 'NA'
#========================================================= 1 = True e 0 = False

def verifica_progressao(l):
    pa = 1
    if max(l) == min(l):
        return('AG')
    rPA = l[1] - l[0]
    for i in range(1, len(l)):
        if l[i] - l[i-1] != rPA:
            pa = 0
            break

    if 0 in l:
        pg = 0
    else:
        pg = 1
        rPG = l[1] / l[0]
        for i in range(1, len(l)):
            if l[i] / l[i-1] != rPG:
                pg = 0
                break
    
    if pa:
        return 'PA'
    elif pg:
        return 'PG'
    else:
        return 'NA'
