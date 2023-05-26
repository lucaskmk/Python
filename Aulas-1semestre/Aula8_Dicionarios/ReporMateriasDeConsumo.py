def precisa_repor(dmat, dsala):
    drepor = {}
    if len(dmat) < 1 or len(dsala) < 1 :
        return drepor
    for nome_sala, dic_mat in dsala.items():
        for material_da_sala, qtd in dic_mat['materiais'].items():
            if material_da_sala in dmat:
                nome_respons = dmat[material_da_sala]['responsavel']
                if qtd < dmat[material_da_sala]['nivel minimo']:
                    if nome_respons not in drepor:
                        drepor[nome_respons] = [{
                                                "sala": nome_sala,
                                                "material":material_da_sala
                                                }]
                    else:
                        drepor[nome_respons] += [{
                                                "sala": nome_sala,
                                                "material":material_da_sala
                                                }]
    return drepor