with open('churras.txt', 'r') as conta:
    total = 0
    conta = conta.readlines()
    print(conta)
    for linhas in conta:
        linhas = linhas.strip()
        item = linhas.split(',')
        qnt = int(item[1])
        pre = float(item[2])
        total += (qnt * pre)
    print(total)