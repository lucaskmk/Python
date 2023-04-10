def classifica_lista(l):
    crs = 0
    dec = 0
#    if min(l) == max(l) or 
    if len(l) < 2:
        return 'nenhum'
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            crs +=1
        if l[i] < l[i-1]:
            dec +=1
            
    if crs == len(l)-1:
        return 'crescente'
    if dec == len(l)-1:
        return 'decrescente'
    else:
        return 'nenhum'
    