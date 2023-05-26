def cria_pecas():
    pecas = []
    for i in range(7):
        for j in range(7):
            if ([i, j] not in pecas) and ([j, i] not in pecas):
                pecas += [[i, j]]
    return pecas

l = cria_pecas()
print(l, len(l))