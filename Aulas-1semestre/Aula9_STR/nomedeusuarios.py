def extrai_nomes_de_usuarios(lemais):
    lnomes = []
    for email in lemais:
        lnomes.append(email[: email.find('@')])
    return lnomes