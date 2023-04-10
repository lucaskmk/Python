def meta_atingida(reclamações, justiça, reclamacao, justica):
    if (reclamacao < reclamações) and (justica < justiça):
        return True
    else:
        return False
#====================================================================
def classifica_pedido(valor, dias, pg, avarias, capital):
    if valor <= 1000 and dias <= 1 and valor <= 150 and avarias.upper() == 'N':
        return 'normal'
    elif  valor <= 1000 and dias <= 1 and valor <= 150 and avarias.upper() == 'S':
        return 'reclamacao'
    elif  valor <= 1000 and dias <= 1 and valor > 150:
        return 'reclamacao'
    elif  valor <= 1000 and dias > 1:
        return 'reclamacao' 
#----------------------------------
    elif valor > 1000 and dias <= 10 and avarias.upper() == 'N' and valor <= 10000 and valor <= 5000 and capital.upper() == 'N':
        return 'normal'
    elif valor > 1000 and dias <= 10 and avarias.upper() == 'N' and valor <= 10000 and valor <= 5000 and capital.upper() == 'S' and pg.upper() == 'P':
        return 'reclamacao'
    elif valor > 1000 and dias <= 10 and avarias.upper() == 'N' and valor <= 10000 and valor <= 5000 and capital.upper() == 'S' and pg.upper() == 'G':
        return 'normal'
    elif valor > 1000 and dias <= 10 and avarias.upper() == 'N' and valor <= 10000 and valor > 5000:
        return 'reclamacao'
    elif valor > 1000 and dias <= 10 and avarias.upper() == 'N' and valor > 10000 :
        return 'justica'
    elif valor > 1000 and dias <= 10 and avarias.upper() == 'S':
        return 'justica'
    elif valor > 1000 and dias > 10:
        return 'justica'

#====================================================================
lmaxre = float(input('limite máximo de reclamações [0.1, 1.0]: '))
lmaxpe = float(input('limite máximo de justiça [0.1, 1.0]: '))
i = 0
resprec = 0
respnorm = 0
respjust = 0
while input('adicionar dados de mais um pedido (S/N)?').upper() == 'S':
    i+=1
    valor = float(input('valor do pedido: '))
    dias = int(input('quantidade de dias em atraso: '))
    pg = input('tamanho do pedido (P/G): ').upper()
    avarias = input('teve alguma avaria (S/N): ').upper()
    capital = input('a entrega é ou não para uma capital(S/N): ').upper()
    respedido = classifica_pedido(valor, dias, pg, avarias, capital)
    if respedido == 'reclamacao':
        resprec += 1
    elif respedido == 'normal':
        respnorm += 1
    elif respedido == 'justica':
        respjust += 1
    print('Pedido classificado como', respedido)

if i > 0:
    print(f"Pedidos por classificação: {resprec: 02} reclamacao, {respnorm: 02} normal, {respjust: 02} justica")

    print(f"Pedidos por classificação: {(100*resprec/i): .2f}% reclamacao, {(100*respnorm/i): .2f}% normal, {(100*respjust/i): .2f}% justica")
    meta = meta_atingida(lmaxre, lmaxpe, resprec, respjust)
    if meta == True:
        print("Meta atingida!")
    else:
        print("Meta nao atingida!")
else:
    pass


