n = 0
ate11 = 0
ate17 = 0
ate25 = 0
ate35 = 0
ate59 = 0
acima60 = 0
idade = int(input('Idade dos pacientes: '))
while idade >= 0:
    n += 1
    if idade <= 11:
        ate11 += 1
    elif idade <= 17:
        ate17 += 1
    elif idade <= 25:
        ate25 += 1
    elif idade <= 35:
        ate35 += 1
    elif idade <= 59:
        ate59 += 1
    elif idade >= 60:
        acima60 += 1
    idade = int(input('Idade dos pacientes: '))

print('0-11 anos:{0: .2f} %' .format(ate11 / n))
print('12-17 anos:{0: .2f} %' .format(ate17 / n))
print('18-25 anos:{0: .2f} %' .format(ate25 / n))
print('26-35 anos:{0: .2f} %' .format(ate35 / n))
print('36-59 anos:{0: .2f} %' .format(ate59 / n))
print('Acima de 60 anos:{0: .2f} %' .format(acima60 / n))