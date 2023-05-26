def distribuir(n, ln):
    import random
    nl = []
    while len(nl) < n:
        rd = random.choice(ln)
        while rd in nl:
            rd = random.choice(ln)
        nl.append(rd)
    return nl