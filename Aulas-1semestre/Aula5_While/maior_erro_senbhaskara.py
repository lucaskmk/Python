import math
maxdif = 0
maxx = 0
x = 0
while x <= 90:
    sinx = (4*x*(180-x)) / (40500-x*(180-x))
    dif =abs(sinx - math.sin(math.radians(x)))
    if dif > maxdif:
        maxdif = dif
        maxx = x
    x += 1
    #dif = max(dif, abs(sinx - math.sin(math.radians(x)))
print(maxx)