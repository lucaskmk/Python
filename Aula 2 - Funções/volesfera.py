def tempo(dias, horas, minutos, segundos): 
    tempototal = ((dias*24 + horas)*60 + minutos)*60 + segundos
    return tempototal
dias = 9
horas = 11
minutos = 15
segundos = 40
print(tempo) 
