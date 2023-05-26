def calcula_porcentagens(dc):
    db = {}
    total = sum(dc.values())
    for i,j in dc.items():
        db[str(i)] = float(j/(total/100))
    return db