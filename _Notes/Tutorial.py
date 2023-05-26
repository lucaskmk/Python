
# O # forma de escrever no codigo que nao atrapalha o funcionamento do codigo

# usa pra uma funcao () dentro oq vai usa
# '' para string
x = 5
print('x')
print(x)
# int()
print('2')
print(int('2')+2)
# contas
print('Usando alguns operadores numéricos:')
print(2 + 3)
print(2 - 3)
print(2 * 3) # multiplicacao
print(2 ** 3) # elevado
print(7 / 3) # dividir 
print(7 // 3) # dividend
print(7 % 3) # sobra 
print((1 + 2) * (-3 - 2)) # conta sempre da esquerda pra direita
# funcao = def + nome da funcao + ( parametros )
# if else e elif
def nome_func(x,y):
    if x == y:
        return True
    else:
        return False
print(nome_func(x,6))
# loop 
    # while if enquanto tiver essa condicao ele entra
i = 0
while i < 10:
    i += 1          # i = i + 1
    print(i)
    # for condicao ja setada
    #for
for j in range(10):
    j += 1
    print(j)
#inerloop
for i in range(4):
    for j in range(4):
        if j == i:
            break
        print(i, j)
# lista 

frutas = ['banana', 'maçã', 'alface', 'pêssego']
print(frutas)
del frutas[2]
print(frutas)
# del apaga e .append adiciona
frutas.append('pêra')

print(frutas)
predeus = ['P','R','E','D','E','U','S'] # 7 ITEWNS NA LISTA
print(predeus[0], predeus[3])
for letra in predeus:
    print(letra)
for posicaoLetra in range(len(predeus)):
    print(posicaoLetra) # numeros
    print(predeus[posicaoLetra]) #numero da lista == o item
def inverte_lista(lista):
    lista2 = []
    s = len(lista)
    for i in range(s):
        lista2 += [lista[s - i - 1]] # === (tasmanho total q e s) - 1 para ir de tras para frente + (-1) pq a lista tem range de um val a menos ex 2 vai para 0 a 1 e nao 1 a 2
    return lista2


# [] em string
    #reverse = [::-1]
snack = "Chocolate cookie."
print(snack[0])
print(snack[9])
print(snack[-1])
print(snack[10:16]) # funciona como un range q inicia do da esquerda = 10 ate o range do da direita 16 ent 15 (lembra range fica menos 1 pq comeca do 0)
print(snack[10:-1]) # -1: since the stop index is excluded in slicing. -1 = ultimo mas como range nm conta o umltimo ent 10 ate penultimo
# Stop value not provided
print(snack[0:]) # Como n tem limite de termino faz tds
# [ AONDE COMECA : AONDE TERMINA-1: quantos em quantos] === for range(inicia, limite-1, pula de n em n)
# Start value not provided (Stop value excluded according to syntax)
print(snack[:-1]) # Como so tem limite de termino faz tds ate (ultimo valor = -1) -1 pq range lembra
print(snack[::-1][0:10]) # 0 a 10 d0 final
print(snack[0:10][::-1], 'teste')
# This is also allowed
print(snack[:]) # n tem limite de comeca e terminar ent td
number_string = "1020304050"
print(number_string[0:-1:2])
print(number_string[::-1]) # n tem limite de comeca e terminar ent td SENDO DESSE TD faz de traz pra frente pq printa ultimo dps menos ultimo em diante
print(number_string[::-2]) # mesma coisa so q ao envez de ser -1 pra traz vai -2 pra traz

#     [x,y,z]  x = inicio        y final - 1 pq e igual range    e   z vais ser de quanto em quanto

# bibliotecas() from math import * )= (impot math) so q sem chamar math. algumacoisa quando usar
# and or
palavra = 'batata'
numero = 7
if len(palavra) == 6 or numero == 8: # 1 valido para funciona
    print("foi")
if len(palavra) == 6 and numero == 8: # 2 validos para funciona
    print("foi")

# dicionario

    #nomedo_dicionario.Keys() == so as chaves q e o tem antes dos :
    #nomedo_dicionario.values() == so os valores q e o tem dps dos :
    #nomedo_dicionario.items() == os dois values e keys
names = {'Ganyu': 1, 'Rem' : 2 ,'Mikan': 3, 'Reze': 4, 'Robin': 5}
for key,value in names.items():
    print(key, value)

nm = ['Ganyu','Rem','Mikan', 'Reze', 'Robin']
game = ['genshin','rezero', 'Danganronpa', 'Chansaw man', 'One Piece']
#5 = len da lista
ranking = {}
for o in range(5):
    #dicionario[key] = value
    ranking[nm[o]] =  game[o]
print(ranking.items())

ranking2 = {}
for i, j in zip(nm, game): # quantidade de coisa do zip tem q ser mesmo das variaveios
    #dicionario[key] = value
    ranking2[i] = j
print(ranking2.items())


