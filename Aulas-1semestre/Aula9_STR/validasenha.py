def valida_senha(s):
    especiais = ['?', '!', '@', '#', '$', '%', '&', '*']
    for caracteres in range(len(s)):
        if s[caracteres] in especiais:
            especiais.remove(s[caracteres])
        if caracteres > 0:
            if (s[caracteres] == s[caracteres-1]) or (len(s) < 8):
                return False
        ultimocaractere = caracteres
    if len(especiais) > 6:
        return False
    return True