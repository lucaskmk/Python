import math
def eh_primo(n):
    if n == 1:
        return False

    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False

    i = 1
    while 2 * i + 1 <= math.sqrt(n):
        if n % (2 * i + 1) == 0:
            return(False)
        i += 1
    return(True)
#===============================

def primos_entre(a, b):
    i = a
    n = 0
    while i <= b:
        if eh_primo(i):
            n += 1
        i += 1
    return n