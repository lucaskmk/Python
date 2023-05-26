def calcula_media(d):
    li =0
    n=0
    for i in d:
        for j in i.values():
            n +=1
            li += j
    return li/n