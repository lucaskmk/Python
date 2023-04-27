data ='1/11/21'
formato ='d/m/a'
def formata_data(data, formato):
    dt = ''
    remover = [',','.','/',';',':','-']
    for estranho in remover:
        data = data.replace(estranho, ' ')
    data.split()
    ordem = [0,0,0]
    for d in data:
        for e in formato:
            if e == 'a':
                ordem[0].append(d)
            if e == 'm':
                ordem[1].append(d)
            if e == 'd':
                ordem[2].append(d)
    if len(ordem[0]) <=2:
        ano = int(ano) + 2000
    for i in ordem:
        if len(dt) == 3 or len(dt) == 6:
            dt += '/'
        else:
            dt += i
    return dt