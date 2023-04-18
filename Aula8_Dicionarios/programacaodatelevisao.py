def quando_passa(dcanais, sfilme):
    dreturn = {}
    for canais in dcanais.keys():
        for horarios, filme in dcanais[canais].items():
            if filme == sfilme:
                if horarios in dreturn:
                    dreturn[horarios] += [canais]
                else:
                    dreturn[horarios] = [canais]
    return dreturn