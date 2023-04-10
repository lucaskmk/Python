def maximo_divisor_comum(a, b):
    i = 1
    mdc = 1
    while i <= min(a, b):
        if (a % i == 0) and (b % i == 0):
            mdc = i
        i += 1
    return mdc