while True:
    entradadojogador = input()
    if entradadojogador == 'a' or entradadojogador == 's' or entradadojogador == 'd' or entradadojogador == 'w':
        print('Entrada válida')
        break
    else:
        print('Entrada do jogador inválida!\nVocê deve digitar a/s/d/w!')