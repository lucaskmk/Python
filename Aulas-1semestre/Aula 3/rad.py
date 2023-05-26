import math
def altura_do_predio(comprimento_sombra, angulo_elevacao):
    # converter o ângulo de graus para radianos
    angulo_radianos = math.radians(angulo_elevacao)
    
    # calcular a altura do prédio usando a fórmula da tangente
    altura_predio = comprimento_sombra * math.tan(angulo_radianos)
    
    return altura_predio