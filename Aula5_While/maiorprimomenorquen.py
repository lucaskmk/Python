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
#======================================
def maior_primo_menor_que(n):
    if n < 2:
        return -1
    i = n
    while i> n or eh_primo(i) == False:
        i -= 1
    return(i)