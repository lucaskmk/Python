
            


# TODO 4 Adicione abaixo a função referente ao exercício: Bússola
def bussola(x_monstro, y_monstro, x_jogador, y_jogador):
    dx = abs(x_monstro - x_jogador)
    dy = abs(y_monstro - y_jogador)
    if dx == 0 and dy == 0:
        return('achou')
    else:
        if x_monstro == x_jogador:
            if y_monstro > y_jogador:
                return('norte')
            elif y_monstro < y_jogador:
                return('sul')
        elif y_monstro == y_jogador:
            if x_monstro < x_jogador:
                return('leste')
            elif x_monstro > x_jogador:
                return('oeste')
        elif dx == dy:
            if y_monstro > y_jogador:
                return('norte')
            elif y_monstro < y_jogador:
                return('sul')
        elif dx < dy:
            if x_monstro > x_jogador:
                return('oeste')
            elif x_monstro < x_jogador:
                return('leste')
        else:
            if y_monstro > y_jogador:
                return('norte')
            elif y_monstro < y_jogador:
                return('sul')