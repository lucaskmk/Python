# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((100, 255, 0))  # Preenche com a cor branca
    cor = (255, 255, 0)
    vertices = [(250, 0), (500, 200), (250, 400), (0, 200)]
    pygame.draw.polygon(window, cor, vertices)
    pygame.draw.circle(window, (0, 0, 255), [250, 200], 150, 0)
    
    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

