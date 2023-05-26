import math
def maior_fator_primo(n):
    for i in range(1, int(math.sqrt(n))+1):
        
        if n % i == 0:
            mx = i
    return mx
print(maior_fator_primo(5))