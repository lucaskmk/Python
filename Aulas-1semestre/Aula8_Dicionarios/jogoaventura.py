def calcula_dano(df):
    ft = 0
    ft += df['força']
    if len(df['equipamentos']) > 0:
        for j in df['equipamentos']:
            ft += j['força']
    return ft