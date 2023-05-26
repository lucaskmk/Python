def login_disponivel(usuario, lista_usuarios):
    if usuario in lista_usuarios:
        n = 0
        for elem in lista_usuarios:
            elem_limpo = ''
            for i in range(len(elem)):
                if elem[i] in ['1','2','3','4','5','6','7','8','9']:
                    break
                else:
                    elem_limpo += elem[i]

            if usuario == elem_limpo:
                n += 1
        return usuario + str(n)
    else:
        return usuario
