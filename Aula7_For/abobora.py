lf = [
  [[2.3, 'kabotia']],
  [[6.2, 'kabotia'], [5.5, 'moranga'], [2.5, 'japonesa'], [1.4, 'moranga']],
  [[4.2, 'moranga'], [9.2, 'moranga'], [14.2, 'moranga']],
  [[5.6, 'kabotia'], [16.2, 'kabotia']],
  [[5.5, 'japonesa'], [12.2, 'japonesa'], [12.3, 'japonesa']],
  [[1.2, 'moranga'], [9.2, 'japonesa'], [8.5, 'japonesa']],
]
especie = 'japonesa'
def maior_abobora(especie, lf):
    maxsize = 0
    posf = -1
    for f in range(len(lf)):
        for a in lf[f]:
            if (a[1] == especie) and (a[0] > maxsize):# >= seria o ultimo valor com mesmas caracteristicas em caso de empate
                maxsize = a[0]
                posf = f
    return posf
print(maior_abobora(especie, lf))