l = []
lista2 = []
d = int(input(''))
while d > 0:
    l += [d]
    d = int(input(''))
lista2 = l[:: -1]
print(lista2)