rodando = True
while rodando:
    palavra = input('')
    if palavra == "fim":
        print("Até a próxima")
        rodando = False
        break
    vogais = ['A','E','I','O','U']
    novpal = ''
    for l in palavra:
        if l.upper() not in vogais:
            novpal += l
    print(novpal)
    print("Até a próxima")