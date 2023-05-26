def calcula_tempo(d1):
    d2 = {}
    for key in d1.keys() :
        d2[key] = (200 / d1[key]) ** 0.5
    return d2