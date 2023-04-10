nj = 2
lp =[
	[1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6],
	[1,1],[1,2],[0,0],[1,4],[1,5],[1,6],[2,2],
	[3,6],[2,4],[2,5],[2,6],[3,3],[3,4],[2,3],
	[3,5],[4,4],[4,5],[0,2],[5,5],[5,6],[0,5]
]

def inicia_jogo(nj, lp):
    dj = {
	'jogadores':
	{},
	'monte':
	[],
	'mesa': []
}
    #jogadores
    njogadores = 0
    for pecas in lp:
        if len(dj['jogadores']) < nj :
            dj['jogadores'][njogadores] = []
            for ate7 in range(7):
                if len(dj['jogadores'][njogadores]) <1:
                    dj['jogadores'][njogadores] = pecas
                if len(dj['jogadores'][njogadores]) >=1:
                    dj['jogadores'][njogadores] += pecas
        njogadores +=1
        if len(dj['jogadores'])>=nj:
            if len(dj['monte']) <1:
                dj['monte'] = pecas
            if len(dj['monte']) >=1:
                dj['monte'] += pecas
    return dj
print(inicia_jogo(nj, lp))