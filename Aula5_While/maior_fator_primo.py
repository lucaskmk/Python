#=========================================================
def maior_fator_primo(n):
    i = 0
    sqrn = math.sqrt(n) 
    if n > 1:
        while sqrn % i != 0 or eh_primo(i) == False:
            i +=1
    return i
print(maior_fator_primo(n))
#=========================================================
def maior_fator_primo(n):
    i = 2
    while i <= n/i:
        if n % i == 0:
            n/= i
        else:
            i+=1
    return n