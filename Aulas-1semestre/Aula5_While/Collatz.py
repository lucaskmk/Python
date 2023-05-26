def collatz(n):
    i = n
    l = [i]
    while i > 1:
        if i % 2 == 0:
            i /= 2
        else:
            i = 3 * i + 1
        l += [i]
    return len(l)


imax = 0
maxlen = 0
for i in range(1, 1000):
    ilen = collatz(i)
    if ilen > maxlen:
        maxlen = ilen
        imax = i

print(imax)