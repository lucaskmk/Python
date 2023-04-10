x = [0, 1]
y = [0, 0]
def gera_direcoes(x,y):
    ln = []
    for i in range(1,len(x)):
        if (x[i]) > (x[i-1]) and (y[i]) == (y[i-1]):
            ln.append('leste')
            return ln
print(gera_direcoes(x,y))