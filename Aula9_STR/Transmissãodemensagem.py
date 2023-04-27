def extract_message(lpacotes):
    mensagem = {}
    frasetotal = []
    for ordem in lpacotes:
        of = []
        of.append(ordem[x] for x in range(len(ordem)) if x >= 0 and x < ordem.find('OF'))
        if of not in range(  x for x in range(len(ordem)) if x > ordem.find('OF') and x < ordem.find('SIZE')  ):
            return []
        size = []
        size.append(ordem[x] for x in range(len(ordem)) if x > ordem.find('SIZE') and x < ordem.find('BEGIN'))
        frase = []
        frase.append(ordem[x] for x in range(len(ordem)) if x > ordem.find('BEGIN') and x < ordem.find('END'))
        if sum(size) != sum(frase):
            return []
        else:
            mensagem[frase] = of
    ordemcorreta = sorted(mensagem.values())
    for frase, numero in mensagem.items():
        for n in range(len(ordemcorreta)) :
            if numero == n:
                frasetotal.append(frase)
    list(frasetotal)