def monta_dicionario0(l1, l2):
    lr = dict()
    for i in range(len(l1)):
        lr[l1[i]] = l2[i]
    return lr

def monta_dicionario1(l1, l2):
    #lr= {chave:item}
    lr = {chave:item for (chave, item) in zip(l1,l2)}
    return lr

def monta_dicionario(l1, l2):
    #lr= {chave:item}
    lr = {l1[i]:l2[i] for i in range(len(l1))}
    return lr