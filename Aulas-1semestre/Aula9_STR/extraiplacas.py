lf = [
  'Os veículos AXX1234 e BCD3E45 foram multados',
  'Digite ABCD123 no google',
  'Veículo apreendidos: EFG5555, DDE2222; quase esqueci do XYZ0A11!'
]
def extrair_placas(lf):
    if lf == []:
        return {}
    nadvbcUHUYH = [',','.','!','?',':',';','-','{','}','(',')','[',']','#']
    ltdn = ['0','1','2','3','4','5','6','7','8','9']
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dplacas = {}
    for f in range(len(lf)):
        ln = lf[f].split(' ')
        for np in range(len(ln)):
            if len(ln[np]) == 7 or len(ln[np]) == 8:
                palavratestada = ''
                for leeeee in ln[np]:
                    if leeeee not in nadvbcUHUYH:
                        palavratestada += leeeee
                if (palavratestada[0] in alfabeto)and(palavratestada[1] in alfabeto)and(palavratestada[2] in alfabeto)and(palavratestada[3] in ltdn) and (palavratestada[4] in ltdn) and (palavratestada[5] in ltdn) and (palavratestada[6] in ltdn):
                    if "antigo" in dplacas:
                        dplacas["antigo"] +=[{           "placa": ln[np],
                                                        "indice_lista_texto": f,
                                                        "indice_palavra": np}]
                    elif "antigo" not in dplacas:     
                        dplacas["antigo"] =[{           "placa": ln[np],
                                                        "indice_lista_texto": f,
                                                        "indice_palavra": np}]                           
                elif (palavratestada[0] in alfabeto)and(palavratestada[1] in alfabeto)and(palavratestada[2] in alfabeto)and(palavratestada[3] in ltdn)and(palavratestada[4] in alfabeto)and(palavratestada[5] in ltdn)and(palavratestada[6] in ltdn):
                    if 'mercosul' in dplacas:
                        dplacas['mercosul'] +=[{           "placa": palavratestada,
                                                        "indice_lista_texto": f,
                                                        "indice_palavra": np}]
                    elif 'mercosul' not in dplacas:     
                        dplacas['mercosul'] =[{           "placa": palavratestada,
                                                        "indice_lista_texto": f,
                                                        "indice_palavra": np}] 
    return dplacas
print(extrair_placas(lf))