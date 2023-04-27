def agrupa_por_idade(d):
    r = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for k, v in d.items():
        if v <= 11:
            r['criança'].append(k)
        if v > 60:
            r['idoso'].append(k)      
        if v > 17 and v <= 59:
            r['adulto'].append(k)
        if v > 11 and v <= 17:
            r['adolescente'].append(k)
    return r