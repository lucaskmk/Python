# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
image = pygame.image.load("assets\img\logo-madfox.png").convert_alpha()
image = pygame.transform.scale(image, (125, 166))
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (10, 10))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

