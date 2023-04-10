def raiz_quadrada(n):
    i = 0
    while n > 0:
        n -= 2 * i + 1
        i += 1
    return i