from statistics import mean

n = int(input('Quantos dias?'))
l = []
for i in range(n):
    p = float(input(f'preco[{i}] '))
    l += [p]
print(round(mean(l),2))
#==================================================================
from statistics import mean

n = int(input('Quantos dias?'))
l = []
for i in range(n):
    p = float(input(f'preco[{i}] '))
    l += [p]
print('O preço médio cobrado foi de ', round(mean(l),2))
#==================================================================
n = int(input('Quantos dias?'))
i = 1
soma = 0
while i <= n:
    p = float(input('preco'))
    i += 1
    soma += p
avg = soma / n
#print('O preço médio cobrado foi de{0: .2f}' .format(avg))
print(f'O preço médio cobrado foi de{avg: .2f}')
