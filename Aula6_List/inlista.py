def intersecao_de_lista(l1, l2):
    ln = []
    for i in l1:
        if i in l2:
            ln.append(i)
    return ln