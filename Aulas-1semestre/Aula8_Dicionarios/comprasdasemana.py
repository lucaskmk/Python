re={
    'Bolo de chocolate': {
        'Leite': 0.25,
        'Óleo': 0.25,
        'Ovo': 2.0,
        'Farinha': 0.5,
        'Açúcar': 0.2,
        'Achocolatado': 0.3
    },
    'Bolinho de chuva': {
        'Óleo': 1.0,
        'Leite': 0.3,
        'Ovo': 3.0,
        'Farinha': 0.6,
        'Açúcar': 0.3
    },
    'Mingau': {
        'Açúcar': 0.1,
        'Maizena': 0.1,
        'Leite': 0.25
    }
}
lp =['Bolinho de chuva', 'Bolo de chocolate', 'Bolinho de chuva']
def compras_da_semana(dr,lp):
    dc = {}
    for item in lp:
        for ingrediente, qtt in dr[item].items():
                if ingrediente not in dc:
                    dc[ingrediente] = qtt
                else:
                    dc[ingrediente] += qtt
    return dc

print(compras_da_semana(re, lp))
