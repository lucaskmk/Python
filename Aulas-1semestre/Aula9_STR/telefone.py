def atualiza_telefone(tf):
    t = ''
    if '-' in tf:
        for i in tf:
            if i != '-':
                t += i
        tf = t
    if tf[0] == '9' and len(tf) == 9:
        return tf
    else:
        tf = '9'+tf
    return tf
print(atualiza_telefone('99999-9999'))
