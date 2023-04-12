def conta_letras(stp):
    ddp = {}
    l= 0
    for i in stp:
        if i in ddp:
            ddp[i] += 1
        else:
            ddp[i] = 1
    return ddp