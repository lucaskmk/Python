def classifica_trigo(l):
    clasific = []
    for i in l:
        if i <= 2:
            clasific.append('T1')
        elif i <= 3:
            clasific.append('T2')
        elif i <= 7:
            clasific.append('T3')
        elif i > 7:
            clasific.append('FT')
    return clasific