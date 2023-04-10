# i assume todos valores de range de n que é igual [0, ...,(n -1)]
def calcula_fibonacci(n):
    f = []
    for i in range(n):
        if i == 0:
            f += [1]
        elif i == 1:
            f += [1]
        else:
            f += [f[i-1] + f[i-2]]
    return f

# funcao recursima == loop do def, exemplo vai procura termo 5 ent prescisa do termo 4 e 3 ent ele tenta dnv pra descobri o 4 q e 3 e 2 ai roda dnv pra descobri o 3 q e 2 e 1 e como ja tem 2 e 1 descobre 3, com isso faz o restoÇ
def calcula_termo_fibonacci(n):
    if n == 1:
        f = 1
    elif n == 2:
        f = 1
    else:
        f = calcula_termo_fibonacci(n - 1) + calcula_termo_fibonacci(n - 2)
    return f

print(calcula_termo_fibonacci(15))