# Juntar elementos de [n] igual em listas --> Elemento : elemento 2
names = ['Ganyu', 'Mikan', 'Reze', 'Robin']
prof = ['genshin', 'Danganronpa', 'Chansaw man', 'One Piece']
my_dictionary = {}

for i in range(3):
    my_dictionary[names[i]] = prof[i]
#              OU 
for (key, value) in zip(names, prof):
    my_dictionary[key] = value
print(my_dictionary)

my_dictionary = {key:value}



#inerloop
for i in range(4):
    for j in range(4):
        if j == i:
            break
        print(i, j)
        
          