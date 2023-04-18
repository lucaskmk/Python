def verifica_ganhador(texto, dicionario):
    dreturn = {}
    lt = texto.split()
    for nome, palavra in dicionario.items():
        for pa in palavra:
            for p in lt:
                p = p.lower()
                if p[-1] in [',','.','?','!',':',';']:
                    p = p[:len(p)-1]
                if p[0] in [',','.','?','!',':',';']:
                    p = p[:0]
                if p == pa:
                    if nome not in dreturn:
                        dreturn[nome] = 1
                    elif nome in dreturn:
                        dreturn[nome] += 1
    return dreturn