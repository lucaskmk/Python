
def modelo(n):
    raiz = n**(1/2)
    raizproxima = int(n**(1/2))
    rpmaior = (raizproxima + 1)**2
    rpmenor = (raizproxima-1)**2
    lista_menor_delta = [abs((raizproxima**2)-n),
                         abs(rpmaior-n), abs(rpmenor-n)]
    menordt = n
    for i in range(len(lista_menor_delta)):
        if lista_menor_delta[i] < menordt:
            menordt = lista_menor_delta[i]
            dt = i
    if dt == 1:
        return (raizproxima + 1)
    elif dt == 2:
        return (raizproxima-1)
    elif dt == 0:
        return int(n**(1/2))


def modelo2(n):
    i=1
    raiz = n**(1/2)
    while i < raiz:
        i += 1
    rpmaior = (i)
    rpmenor = (i-1)
    if abs((rpmaior**2)-n) < abs((rpmenor**2)-n):
        return rpmaior
    else:
        return rpmenor


print(modelo(120.11), modelo(40.7), modelo(26),modelo(4))
print(modelo2(120.11), modelo2(40.7), modelo2(26),modelo2(4))

# 22
