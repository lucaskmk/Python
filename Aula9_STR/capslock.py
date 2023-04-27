def capsLock(strg):
    frase = ''
    for l in strg:
        if l.isupper() == True:
            frase += l.lower()
        elif l.isupper() == False:
            frase += l.upper()
    return frase