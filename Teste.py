lt = 121.5
ness =29
esp = 2
i=1
estante = esp + ness
while estante < 121.5: 
    i+=1
    estante += esp + 23
    if estante > 121.5:
        i-=1
        estante -= esp + 23
        sobra = estante - lt
        break
        
print(i, estante, abs(sobra), '1')

#=====================================

lt = 121.5
ness =29
esp = 2
total_de_estantes =1
estante = esp + ness
cm = 20
while cm % 121.5 != 0: 
    cm += 0.01 
        
print(cm)