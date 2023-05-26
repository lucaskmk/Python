def dias_do_ano(dia):
    n = int(dia[0] + dia[1])
    m = int(dia[3] + dia[4])-1
    diastotal = (n-1)
    dmes =[31,28,31,30,31,30,31,31,30,31,30,31]
    for dias in range(m):
        diastotal += dmes[dias]
    return diastotal