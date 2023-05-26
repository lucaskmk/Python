def anagrama(p1, p2):
    if len(p1) != len(p2):
        return False
    letras = {}
    for i in p1:
        if i in letras:
            letras[i] += 1
        else:
            letras[i] = 1
    for j in p2:
        if j not in letras.keys() or letras[j] < 1:
            return False
        if j in letras:
            letras[j] -= 1
    return True

p1 = 'mora'
p2 ='amor'
print(anagrama(p1, p2))