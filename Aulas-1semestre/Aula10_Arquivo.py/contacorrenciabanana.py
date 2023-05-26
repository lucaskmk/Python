with open('macacos-me-mordam.txt', 'r') as mac:
    macs = mac.read().strip()
    tb = 0
    ltotal = macs.replace('\n',' ').split(' ')
    for pal in ltotal:
        if pal.lower() == 'banana':
            tb += 1
    print(tb)