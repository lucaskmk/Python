def calcula_idade(datanas, dataat):
    dif_dd = int(dataat[0:2]) - int(datanas[0:2])
    dif_mm = int(dataat[3:5]) - int(datanas[3:5])
    dif_aa = int(dataat[6:]) - int(datanas[6:])
    return(dif_aa - (dif_mm < 0) * 1 - ((dif_mm == 0) * (dif_dd < 0)) * 1)