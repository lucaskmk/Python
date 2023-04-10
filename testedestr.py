def fatorial(n):
    i = 0
    f = 1
    while i < n:
        i += 1
        f *= i
    return f
def calcula_serie(n):
    i=0
    while i < n:
        c = ((2**i)*(fatorial(1+i)))/(5*(3**i))
        i+=1
    return c

print(calcula_serie(1))   
    
    