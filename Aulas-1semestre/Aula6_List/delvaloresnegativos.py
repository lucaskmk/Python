def zera_negativos(listan):
    for i in range(len(listan)):
        if listan[i] < 0:
            listan[i] = 0
    return listan