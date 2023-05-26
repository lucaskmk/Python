def conta_palavras(texto):
    dreturn = {}
    lt = texto.split()
    for st in lt:
        st = st.lower()
        if st[-1] in [',','.','?','!',':',';']:
            st = st[:-1]
        if st[0] in [',','.','?','!',':',';']:
            st = st[:0]
        if st not in dreturn:
            dreturn[st] = 1
        else: 
            dreturn[st] += 1
    return dreturn