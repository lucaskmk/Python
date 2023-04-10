def pet_pode_viajar(lpet, llimites, vend):
    esp=0
    if lpet[len(lpet)-1] == 'N':
        return False
    for dim in range(3):
        if lpet[4][dim] > llimites[2][dim]:
            return False
    if (lpet[2] + lpet[3]) > llimites[1]:
        return False
    for i in range(len(vend)):
        if 'pet_cabine' in vend[i][1]:#iverso eu era burro e tava fazendo == mas como n sei limite de vend[x][1] assim q ta e melhor
            esp += 1
    if abs(llimites[0]-esp) < 1:
        return False
    return True