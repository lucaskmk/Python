def alunos_impares(lista):
#[lista[x] if x % 2 == 1 else 'skipped' for x in range(len(lista))]
#posicao range(len
    return [lista[x] for x in range(len(lista)) if x % 2 == 1]