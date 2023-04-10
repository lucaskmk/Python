matriz = [[1,2,3], [4,5,6], [7,8,9]]
l = []
for linha in matriz:
    for elemento in range(len(linha)):
        l += [linha[elemento]]
print(max(l))


#[elemento] sem range ========================  [linha[elemento]] com range
matriz = [[1,2,3], [4,5,6], [7,8,9]]
l = []
for linha in matriz:
    for elemento in linha:
        l += [elemento]
print(max(l))
