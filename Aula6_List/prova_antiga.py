l = ['lista', 'de', 'palavras']
n=2
def a(l,n):
    nl = []
    for i in range(len(l)):
        temp = ''
        for j in range(n):
            temp += l[i][j]
        nl += [temp]
        #ao envez de for da pra fazer isso tbm -> nl += [l[i][0:n]]
    return nl
print(a(l,n))
#============================================================
a = ('casa')
l = []
for i in range(len(a)-2):
    if a[i] == a[i+2]:
        l += [a[i] + a[i+1] + a[i+2]]
print(l)


a = ('abastecer')
l =[]
if len(a) < 3:
    print ('word is too short!')
for i in range(2, len(a)):
    triade = a[i-2] + a[i-1] + a[i]
    if triade == triade[::-1]:
        l += [triade]
print(l)


