def verifica_jogo_da_velha(jogo):
    for i in range(3):
        if (jogo[i][0] == 'O' and jogo[i][1] == 'O' and jogo[i][2] == 'O') or ( jogo[0][i] == 'O' and jogo[1][i] == 'O' and jogo[2][i] == 'O') or ( jogo[0][0] == 'O' and jogo[1][1] == 'O' and jogo[2][2] == 'O') or  (jogo[0][2] == 'O' and jogo[1][1] == 'O' and jogo[2][0] == 'O'):
            return 'O'
        elif (jogo[i][0] == 'X' and jogo[i][1] == 'X' and jogo[i][2] == 'X') or ( jogo[0][i] == 'X' and jogo[1][i] == 'X' and jogo[2][i] == 'X') or ( jogo[0][0] == 'O' and jogo[1][1] == 'X' and jogo[2][2] == 'O') or  (jogo[0][2] == 'X' and jogo[1][1] == 'X' and jogo[2][0] == 'X'):
            return 'X'
    else:
        return'V'