def calcula_escola(l):
    nota_total = 0
    for quesito in l:
        nota_total += sum(quesito) - min(quesito)
    return nota_total
            