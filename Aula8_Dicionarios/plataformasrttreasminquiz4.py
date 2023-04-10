def series_por_streaming(plataformas, atores, titulos):
    series = {}
    for plataforma, ator, titulo in zip(plataformas, atores, titulos):
        if plataforma not in series:
            series[plataforma] = []
        series[plataforma].append({'performer': ator, 'title': titulo})
    return series