#def esta_na_lista(pais, lista):
#    for item in lista:
#        if pais == item[0]:
#            return True
#    return False

def esta_na_lista(pais, lista):
    return(pais in [lista[i][0] for i in range(len(lista))])
