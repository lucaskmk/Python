import random
import math

# ---------------------------------------------------------- #

def sorteia_posicao_do_monstro(largura, altura):
    return random.randint(0, largura-1), random.randint(0, altura-1)

def sorteia_posicao_do_jogador(largura, altura, x_monstro, y_monstro):
    # Sorteando posição inicial do jogador no tabuleiro
    # Faz validação para que não seja sorteada a mesma posição em que o monstro se encontra
    sorteia_pos = True
    while sorteia_pos:
        x_jogador = random.randint(0, largura-1)
        y_jogador = random.randint(0, altura-1)
        if x_jogador != x_monstro or y_jogador != y_monstro:
            sorteia_pos = False
    return x_jogador, y_jogador

def sorteia_posicao_da_porta(largura, altura, x_monstro, y_monstro, x_jogador, y_jogador):
    # Sorteando posição inicial da porta no tabuleiro
    # Faz uma validação para que não seja sorteada a mesma posição em que o monstro e a porta se encontram
    sorteia_pos = True
    while sorteia_pos:
        x_porta = random.randint(0, largura-1)
        y_porta = random.randint(0, altura-1)
        if (x_porta != x_monstro or y_porta != y_monstro) and  (x_porta != x_jogador or y_porta != y_jogador):
            sorteia_pos = False
    return x_porta, y_porta

def dica(x_monstro, y_monstro, x_jogador, y_jogador):
    distancia = math.sqrt((x_jogador - x_monstro)**2 + (y_jogador-y_monstro)**2)
    if distancia <= 2:
        return 'quente'
    elif distancia <= 3:
        return 'morno'
    elif distancia <= 4:
        return 'fresco'
    else:
        return 'frio'

def imprime_tabuleiro(x_monstro, y_monstro, x_jogador, y_jogador,x_porta, y_porta, largura, altura, debug):
    tabuleiro = ''
    linha1 = f"   {'  '.join([f'{i}' for i in range(largura)])}"
    tabuleiro += f'{linha1}\n'
    tabuleiro += f'{"_"*len(linha1)}\n'

    for y in range(altura):
        linha = f'{y}| '
        for x in range(largura):
            if x == x_jogador and y == y_jogador:
                linha += f'J  '
            elif x == x_monstro and y == y_monstro and debug:
                linha += f'M  '
            elif x == x_porta and y == y_porta and debug:
                linha += f'P  '
            else:
                linha += f'_  '

        tabuleiro += f"{linha}\n"
    return tabuleiro

# TODO 4 Adicione abaixo a função referente ao exercício: Bússola

def bussola(x_monstro, y_monstro, x_jogador, y_jogador):
    dx = abs(x_monstro - x_jogador)
    dy = abs(y_monstro - y_jogador)
    if x_jogador == x_monstro and y_jogador ==  y_monstro:
        return('achou')
    else:
        if dx == dy:
            if y_monstro > y_jogador:
                return('norte')
            elif y_monstro < y_jogador:
                return('sul')
        elif x_monstro == x_jogador:
            if y_monstro > y_jogador:
                return('norte')
            elif y_monstro < y_jogador:
                return('sul')
        elif y_monstro == y_jogador:
            if x_monstro < x_jogador:
                return('leste')
            elif x_monstro > x_jogador:
                return('oeste')
        elif dx < dy:
            if x_monstro < x_jogador:
                return('leste')
            elif x_monstro > x_jogador:
                return('oeste')
        elif dy < dx:
            if y_monstro < y_jogador:
                return('sul')
            elif y_monstro > y_jogador:
                return('norte')
# Largura e altura do tabuleiro
largura = 8
altura = 8

# Sorteia posição do monstro
x_monstro, y_monstro = sorteia_posicao_do_monstro(largura, altura)

# Sorteia posição do Jogador
x_jogador, y_jogador = sorteia_posicao_do_jogador(largura, altura, x_monstro, y_monstro)

# Sorteia posição da Porta
x_porta, y_porta = sorteia_posicao_da_porta(largura, altura, x_monstro, y_monstro, x_jogador, y_jogador)

# ---------------------------------------------------------- #
jogando = True
debug = False # Com o debug igual a True a posição do monstro e da porta são visíveis
while jogando:

    tabuleiro = imprime_tabuleiro(x_monstro, y_monstro, x_jogador, y_jogador, x_porta, y_porta, largura, altura, debug)
    print(tabuleiro)

    # TODO 1 Coloque aqui o seu código do exercício: Valida entrada do Jogador

    while True:
        entradadojogador = input()
        if entradadojogador == 'a' or entradadojogador == 's' or entradadojogador == 'd' or entradadojogador == 'w':
            print('Entrada válida')
            break
        else:
            print('Entrada do jogador inválida!\nVocê deve digitar a/s/d/w!')

    # TODO 2 Adicione abaixo o código referente ao exercício: Atualiza posição do jogador abaixo

    if entradadojogador == 'w':
        y_jogador -= 1
    if entradadojogador == 's':
        y_jogador += 1
    if entradadojogador == 'a':
        x_jogador -= 1
    if entradadojogador == 'd':
        x_jogador += 1
    print((x_jogador, y_jogador))
    
    # TODO 3 Adicione abaixo o código referente ao exercício: Verifica se o Jogador encontrou a porta
    sim = False
    if x_jogador == x_porta and y_jogador == y_porta:
        print("Achou a porta!")
        jogando = False
        sim = True
    # TODO 5 Adicione abaixo o código referente ao exercício: Movimenta Monstro
    elif sim == False:
        movimento = bussola(x_monstro, y_monstro, x_jogador, y_jogador)
        if movimento == 'norte':
            y_monstro -= 1 
        elif movimento == 'sul':
            y_monstro += 1
        elif movimento == 'leste':
            x_monstro += 1
        elif movimento == 'oeste':
            x_monstro -= 1   
    if sim == False:
        print((x_monstro, y_monstro))
    
    # TODO 6 Adicione abaixo o código referente ao exercício: Verifica se monstro encontrou o jogador
    movimento = bussola(x_monstro, y_monstro, x_jogador, y_jogador)
    if movimento == 'achou':
        print('O monstro te achou!')
        jogando = False
    else:
        print(dica(x_monstro, y_monstro, x_jogador, y_jogador))
#print('({0}, {1})'.format(x_monstro, y_monstro))
        
    # TODO 6 Adicione abaixo o código referente ao exercício: Verifica se monstro encontrou o jogador