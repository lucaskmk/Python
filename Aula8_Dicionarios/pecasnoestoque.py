def tem_estoque(dn, dpe):
    totalvalido = 0
    for pecas,n in dn.items():
        for estoque, quantidade in dpe.items():
            if pecas == estoque and quantidade >= n:
                totalvalido +=1
    if totalvalido == len(dn):
        return True
    return False