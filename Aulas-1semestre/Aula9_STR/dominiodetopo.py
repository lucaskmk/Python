def usuarios_por_pais(lusers, dpais):
    dreturn = {}
    for sigla, pais in dpais.items():
        for user in lusers:
            if user[-2:] == sigla:
                if pais not in dreturn:
                    dreturn[pais] = [user[: user.find('@')]]
                else:
                    dreturn[pais] += [user[: user.find('@')]]
    return dreturn