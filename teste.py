l1 = [ [2, 23] , [1, 32], [1, 10], [3, 23] ]
l2 = [ [2, 10], [0, 21, 24], [1, 30, 33], [3, 22, 23] ]
def valores_a_pagar(l1, l2):
    ln= []
    for i in range(len(l1)):
        for o in range(len(l1)):
            if i == l2[o][0]:#procuro o passageiro
                if (len(l2[i])-1) > l1[i][0]:#-1 tira o numero do passageiro 
                    j = abs((len(l2[i])-1) - (l1[i][0]))#n malas extras         
                    ln.append(300*j)
                else:
                    ln.append(0)
                for k in range(1, len(l2[i])):
                    if l2[i][k] > l1[i][1]:#ver se os elementos sao maiores que oeso da bagagem, levando 
                        taxa = l2[i][k] - l1[i][1]
                        ln.append(50*taxa)
                    else:
                        ln.append(0)
    return ln
print(valores_a_pagar(l1, l2))