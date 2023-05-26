def acha_bigramas(pal):
    biag = []
    st = ''
    for letra in pal:
        st += letra
        if len(st) == 2:
            if st not in biag:
                biag.append(st)
                st = letra
            else:
                st = letra
    return biag
pal = 'babador'
print(acha_bigramas(pal))