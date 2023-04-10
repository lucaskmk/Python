def lista_em_zigue_zague(lista):
    if len(lista) < 2:
        return True

    if lista[1] > lista[0]:
        last = 'maior'
    elif lista[1] < lista[0]:
        last = 'menor'
    else:
        return False

    for i in range(2, len(lista)):
        if (last == 'maior') and (lista[i] >= lista[i-1]):
            return False
        elif (last == 'menor') and (lista[i] <= lista[i-1]):
            return False
        else:
            if lista[i] < lista[i-1]:
                last = 'menor'
            else:
                last = 'maior'
    return True