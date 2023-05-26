ma = [[0,2],[2,1],[1,6],[6,5],[5,3]]
ps = [[1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6]]
def posicoes_possiveis(ma,ps):
    rl = []
    if len(ma) == 0:
        for p in range(len(ps)):
            rl.append(p)
    else:
            for i in range(len(ps)):
                if (ma[0][0] == ps[i][0]) or (ma[len(ma)-1][1] == ps[i][0]) or (ma[0][0] == ps[i][1]) or (ma[len(ma)-1][1] == ps[i][1]):
                    rl.append(i)

    rl = sorted(set(rl))        
    return rl
print(posicoes_possiveis(ma,ps))