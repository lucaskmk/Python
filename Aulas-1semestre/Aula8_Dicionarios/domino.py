def verifica_ganhador(mesa):
    for i in mesa:
        if len(mesa[i]) == 0:
            return i
    return -1