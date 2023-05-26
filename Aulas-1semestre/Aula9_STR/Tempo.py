def quanto_tempo(ltemp):
    s = 0
    m = 0
    h = 0
    cont = 0
    for tempo in ltemp:
        if 'h' in tempo:
            h += int(tempo[0:tempo.find('h')])
            tempo = tempo.replace(tempo[0:tempo.find('h')+1], '')
        if 'm' in tempo:
            m += int(tempo[0:tempo.find('m')])
            tempo = tempo.replace(tempo[0:tempo.find('m')+1], '')
        if 's' in tempo:
            s += int(tempo[0:tempo.find('s')])
            tempo = tempo.replace(tempo[0:tempo.find('s')+1], '')
    if s >= 60:
        while s >= 60:
            s-=60
            cont += 1
            print(s)
    m += cont
    cont = 0
    if m >= 60:
        while m >= 60:
            m-=60
            cont += 1
    h += cont
    frase = ''
    if h > 0:
        frase += str(h)+'h'
    if m > 0:
        frase += str(m)+'m'
    if s > 0:
       frase += str(s)+'s'

    return frase