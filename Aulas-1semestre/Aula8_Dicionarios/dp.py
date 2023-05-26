def notas_dp(notas):
    ldp = []
    for boletin in notas:
        dp = (boletin['PI'] + boletin['PF']) / 2
        if dp < 5:
            ldp.append(boletin['matricula'])
    return ldp
