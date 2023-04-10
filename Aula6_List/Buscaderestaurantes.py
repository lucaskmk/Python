
def busca_restaurantes(res, p, valor):
    f = []
    for i in range(len(res)):
            if p == "culinaria":
                if res[i][1] == valor:
                    f.append(res[i][0])
                    
            if p ==  "ambiente":
                if res[i][2] == valor:
                    f.append(res[i][0])
                    
            if p ==  "preco":
                if res[i][3] <= valor:
                    f.append(res[i][0])
    return f