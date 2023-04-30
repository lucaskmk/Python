def conserta_teclado(tk):
    tk = tk.lower()
    rst = ''    
    for i in range(len(tk)):
        if i == 0:
            rst += tk[i]
            lp = tk[i]
        elif tk[i] != lp:
            rst += tk[i]
            lp = tk[i]
    return rst

