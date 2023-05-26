def converteHora(hrelog):
    if hrelog[0:2] == '12':
        horario = hrelog +' PM'
    elif int(hrelog[0:2]) > 12:
        if int(hrelog[0:2]) >= 22:
            horario = (str(int(hrelog[0:2]) - 12 )+ hrelog[2:]) +' PM'
        else:
            horario = '0' + (str(int(hrelog[0:2]) - 12 )+ hrelog[2:]) +' PM'
    else:
        horario = hrelog +' AM'
    return horario