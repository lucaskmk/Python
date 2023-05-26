with open('texto.txt', 'r') as arq:
    arq1 = arq.read().strip()
    arq2 = arq1.replace('\n',' ').split(' ')
    print(len(arq2))