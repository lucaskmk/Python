def soma_multiplos(x, y):
    lim = 10 * max(x, y)
    i = 0
    soma = 0
    nums = []
    while i <= lim:
        if (i % x == 0) or (i % y == 0):
            soma += i
            nums += [i]
        i += 1
    return('Valores a serem somados:', nums, 'Saída (total):', soma)