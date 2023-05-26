import random

dinheiro = 100
print(dinheiro)
while dinheiro > 0:
    resultado = 'perdeu'
    valor_apostado = int(input('valor apostado: '))
    if valor_apostado == '0' :
        break
    elif valor_apostado > dinheiro:
        break
    else:
        oqueapostar = input('aposta é um número (n) / par (p) / impar (i): ').upper()
        if oqueapostar in ['N', 'P', 'I']:
            sorteio = random.randint(0, 36)
            if oqueapostar == 'N':
                oqueapostar = int(input('entre um número entre 1 e 36: '))
                if 1 <= oqueapostar <= 36:
                    if oqueapostar == sorteio:
                        resultado = 'ganhou'
                        dinheiro += 35 * valor_apostado
                else:
                    resultado = 'erro'
            elif oqueapostar == 'P':
                if sorteio % 2 == 0:
                    resultado = 'ganhou'
                    dinheiro += valor_apostado
            elif oqueapostar == 'I':
                if sorteio % 2 == 1:
                    resultado = 'ganhou'
                    dinheiro += valor_apostado
            if resultado == 'perdeu':
                dinheiro -= valor_apostado
            #print('número sorteado:', sorteio)
            print(dinheiro)