def calcula_total_da_nota(l1, l2):
    total = 0
    for i in range(len(l1)):

        total += l1[i] * l2[i]   
    return total