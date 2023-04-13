def explodedm(dm):
    dm2 = {}
    #=============explode primeira vez
    for empresa in dm.keys():
        vdm = dm[empresa]['valor de mercado']
        associados = {}
        for associado, valor in dm[empresa]['associados'].items():
            if associado in dm.keys():
                for a, v in dm[associado]['associados'].items():
                    if a in associados:
                        associados[a] += valor/100 * v
                    else:
                        associados[a] = valor/100 * v
            else:
                if associado in associados:
                    associados[associado] += valor
                else:
                    associados[associado] = valor

        dm2[empresa] = {'valor de mercado' : vdm,
                        'associados' : associados}
    # fora do loop verifica se vai ter que rodar dnv ou n se sim roda a funcao em si, isso chama de funcao recursiva, deu pra fazer no ex de fibonaci
    #=============verifica se explode 
    again = False
    for empresa in dm2.keys():
        for associado in dm2[empresa]['associados'].keys():
            if associado in dm.keys():
                again = True
                break
    if again:
        #============= explode x vezes
        return explodedm(dm2)
    else:
        #nao explode mais
        return dm2

# fiz esse primeiro mas tinmha o problema q  afuncao n tava explodida(tinha impresa nos associados)
def soma_investimento(dm):
    # ja explodido
    dm_explodido = explodedm(dm)
    va = {}
    for fundo in dm_explodido.keys():   
        for investidor, valinvestido in dm_explodido[fundo]['associados'].items():
            totalinvest = (valinvestido/100)*dm_explodido[fundo]['valor de mercado']                         
            if investidor in va:
                va[investidor] += totalinvest
            else:
                va[investidor] = totalinvest
    return va



#=====================================
def soma_investimento(empresas):
    final = {}
    le = []

    for e in empresas.keys():
        empresa_atual = empresas[e]
        le.append(e)
        valor_total = empresa_atual['valor de mercado']
        for r in empresa_atual['associados']:
            if r not in final:
                final[r] = 0
                final[r] += (empresa_atual['associados'][r]/100)*valor_total
            else:
                final[r] += (empresa_atual['associados'][r]/100)*valor_total

    while any(i in final for i in le):
        for i in le:
            if i in final:
                empresa_atual = empresas[i]
                valor_total = final[i]
                for r in empresa_atual['associados']:
                    if r not in final:
                        final[r] = 0
                        final[r] += (empresa_atual['associados'][r]/100)*valor_total
                    else:
                        final[r] += (empresa_atual['associados'][r]/100)*valor_total
                del final[i]
    return final