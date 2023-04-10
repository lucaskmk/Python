def PiWallis(n):
    i = 0
    num = 0
    den = 1
    pi = 1
    while i < n:
        i+=1
        if i % 2 == 1:
            num += 2
        else:
            den += 2
        pi *= (num / den)
    pi *= 2
    return pi