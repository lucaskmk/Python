def quantos_uns(numero):
    i = 0
    for digito in str(numero)  :
        if digito == '1':
            i += 1
    return i 