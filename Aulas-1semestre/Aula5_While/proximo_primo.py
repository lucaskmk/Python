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

#========================================
def proximo_primo(n):
    if n < 2:
        return(2)
    
    achou = False
    if n % 2 == 0:
        n2 = n + 1
    else:
        n2 = n + 2
    
    while not achou:
        if eh_primo(n2):
            achou = True
        else:
            n2 += 2
    return(n2)

#========================================
def proximo_primo(n):
    if n < 2:
        return(2)
    i = n + 1
    while not eh_primo(i):
        i += 1
    return(i)
#========================================
def proximo_primo(n):
    if n < 2:
        return(2)
    i = 0
    while i <= n or eh_primo(i) == False:
        i += 1
    return(i)

#========================================
def proximo_primo(n):
    if n < 2:
        return(2)
    
    achou = False
    if n % 2 == 0:
        n2 = n + 1
    else:
        n2 = n + 2
    
    while not achou:
        if eh_primo(n2):
            achou = True
        else:
            n2 += 2
    return(n2)