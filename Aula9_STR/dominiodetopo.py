ldusers = ['usuario1@insper.edu.br', 'usuario2@uma.pt', 'usuario3@kth.se', 'usuario4@usp.br'],
{
    'pt': 'Portugal',
    'br': 'Brasil',
    'se': 'Suécia'
}
           
def usuarios_por_pais(ldusers):
    dreturn = {}
    for user in ldusers[0]:
        for sigla, pais in ldusers[1].items():
            if user[-2:] == sigla:
                if pais not in dreturn:
                    dreturn[pais] = user[0:user.find('@')]
                else:
                    dreturn[pais] += user[0:user.find('@')]
    return dreturn

print(usuarios_por_pais(ldusers))