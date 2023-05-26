def valida_exp(exp):
    exp_cln = exp.replace(' ','')
    exp_new = 0
    i = 0
    j = 0
    k = 0
    sinal = ''
    while i < len(exp_cln):
        while exp_cln[i] == 'I':
            if i >= exp_cln.find('='):
                k += 1
                break
            j += 1
            i += 1
        if exp_new == 0:
            exp_new = j
        else:
            if sinal == '+':
                exp_new += j
            elif sinal == '-':
                exp_new -= j
            elif sinal == '*':
                exp_new *= j
            elif sinal == '/':
                exp_new /= j
        if i != len(exp_cln):
            sinal = exp_cln[i]
        j = 0
        i +=1
    return exp_new==k

#============= Expresao dos dois lados ===========================================================

def calcula_exp(exp):
    exp_cln = exp.replace(' ','')
    exp_new = 0
    i = 0
    j = 0
    sinal = ''
    while i < len(exp_cln):
        while exp_cln[i] == 'I':
            j += 1
            i += 1
            if i == len(exp_cln):
                break

        if exp_new == 0:
            exp_new = j
        else:
            if sinal == '+':
                exp_new += j
            elif sinal == '-':
                exp_new -= j
            elif sinal == '*':
                exp_new *= j
            elif sinal == '/':
                exp_new /= j
        if i != len(exp_cln):
            sinal = exp_cln[i]
        j = 0
        i +=1
    return exp_new

def valida_exp(exp):
    a = calcula_exp(exp[0 : exp.find('=')])
    b = calcula_exp(exp[exp.find('=') + 1 : len(exp)])
    return(a==b)

exp = 'I*I *I * II + I= III'
x = valida_exp(exp)
print(x)