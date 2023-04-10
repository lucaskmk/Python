valor = int(input(''))
enter = input('')
while enter != '=':
    if enter in ['+','-','*','/','=']:
        numero = int(input(''))
        if enter == '+':
            valor += numero
        elif enter == '-':
            valor -= numero
        elif enter == '*':
            valor *= numero
        elif enter == '/':
            valor /= numero
        if enter != '=':
            enter = input('')
    else:
        print("Deveria ser um dos seguintes operadores: + - / * ou o =")
        enter = input('')
print(valor)

    
    
def valida_entradas(lista):
    if len(lista) < 2:
        return False
    if lista[-1] != '=':
        return False
    for i in range(1,len(lista), 2):
        if i == len(lista)-1:
            if lista[i] != '=':
                return False
        elif lista[i] not in ["-", "*", "/", "**", "//", "%", '+']:
            return False
    return True