i = 0
lst = list()
# x = list() é o mesmo que x = []
while i < 5:
    lst += [int(input(f'[{i+1}]: '))]
    print(lst)
    i += 1
#for i in [1,4,5,43,23,243,256,111,23,45]:
#    if i % 2 == 0:
#        print(i)
print('libia' in ['libia', 'egito', 'india', 'japao'])  

print([x if x % 2 == 0 else 2*x for x in range(10)])


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


#quer posicao usa range len

def alunos_impares(lista):
#[lista[x] if x % 2 == 1 else 'skipped' for x in range(len(lista))]
#posicao range(len
    return [lista[x] for x in range(len(lista)) if x % 2 == 1]
#=================================================================================================
frutas = ['banana', 'maçã', 'alface', 'pêssego']

print(frutas)


del frutas[2]

print(frutas)

# del apaga e .append adiciona
frutas.append('pêra')

print(frutas)