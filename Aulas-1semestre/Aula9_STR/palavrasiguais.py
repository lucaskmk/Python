def palavras_sao_iguais(pa):
    re = pa.split('-')
    if len(re) < 2 :
        return False
    elif re[0] == re[1] :
        return True
    else:
        return False