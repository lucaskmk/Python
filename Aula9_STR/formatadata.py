def formata_data(data, formato):
    sep = formato[1]
    dados_data = data.split(sep)
    dict_data = {
        str(formato[0]) : dados_data[0],
        str(formato[2]) : dados_data[1],
        str(formato[4]) : dados_data[2],
    }
    if len(dict_data['a']) <= 2:
        dict_data['a'] = str(int(dict_data['a']) + 2000)
    if len(dict_data['m']) == 1:
        dict_data['m'] = '0' + dict_data['m'] 
    if len(dict_data['d']) == 1:
        dict_data['d'] = '0' + dict_data['d'] 
    return(dict_data['a']+'-'+dict_data['m']+'-'+dict_data['d'])