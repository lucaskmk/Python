def palavras_com_tamanho_crescente(lista):
    ultimafrase = ''
    for frase in lista:
        if len(frase) <= len(ultimafrase):
            return False
            break
        ultimafrase = frase
    return True