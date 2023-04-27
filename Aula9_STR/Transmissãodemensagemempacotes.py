def extract_message(lpacotes):
    dictr = {}
    msg_fim = ''
    for msg in lpacotes:
        sz1 = msg[0 : msg.find('OF')]
        sz2 = msg[msg.find('OF') + 2: msg.find('SIZE')]
        sz3 = msg[msg.find('SIZE') + 4: msg.find('BEGIN')]
        txt = msg[msg.find('BEGIN') + 5: len(msg)-3]
        if len(txt) != int(sz3):
            return 'msg_fim'
        dictr[int(sz1)-1] = txt

    if len(dictr) != int(sz2):
        return msg_fim
    
    for i in range(len(dictr)):
        msg_fim += dictr[i]

    return msg_fim