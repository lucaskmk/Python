def eh_respiravel(ar):
    oxigen = 0
    n = 0
    for camada in ar:
        for elemento in camada:
            if 'O' in elemento:
#            if ar[camada][elemento] == 'O':
                oxigen+=1
            n +=1
    porcentagem = oxigen / n
    if porcentagem >= 0.20:
        return True
    else:
        return False


        