import pygame
import sys
<<<<<<< Updated upstream

# Classe para representar o chão
class Chao:
    def __init__(self, x, y, largura, altura, cor):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

# Classe para representar o personagem
class Personagem:
    def __init__(self, x, y, largura, altura, cor):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor
        self.velocidade = 1
        self.gravidade = 0.01
        self.velocidade_vertical = 0
        self.altura_do_salto = 0
        self.pulando = False

    def mover(self, teclas):
        if teclas[pygame.K_a]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_d]:
            self.rect.x += self.velocidade

    def aplicar_gravidade(self):
        self.velocidade_vertical += self.gravidade
        self.rect.y += self.velocidade_vertical

    def pular(self):
        if not self.pulando:
            self.pulando = True
            self.velocidade_vertical = -self.altura_do_salto

    def colisao_chao(self, chao):
        if self.rect.colliderect(chao.rect):
            self.rect.y = chao.rect.y - self.rect.height
            self.velocidade_vertical = 0
            self.pulando = False

# Inicialização do Pygame
pygame.init()

# Definir as dimensões da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

# Definir as cores
preto = (0, 0, 0)
branco = (255, 255, 255)
=======
from Cena1 import Chao, Personagem, tela, Cores, largura

# Definir as cores
preto = preto = (0, 0, 0)
branco = branco = (255, 255, 255)
vermelho = vermelho = (255, 0, 0)
>>>>>>> Stashed changes

# Criar instâncias do chão e do personagem
chao = Chao(0, 500, largura, 20, branco)
personagem = Personagem(100, chao.rect.y - 50, 50, 50, branco)

# Defina essas variáveis antes do loop principal do jogo:
velocidade_vertical = 0.0  # Inicialize com zero
fator_desaceleracao = 0.95  # Ajuste o valor conforme necessário

# Antes do loop principal, adicione uma variável para rastrear se o personagem está no chão
no_chao = True

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                personagem.pular()

    # Capturar as teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Aplicar desaceleração vertical
    velocidade_vertical *= fator_desaceleracao

    # Aplicar gravidade
    personagem.aplicar_gravidade()

    # Verificar colisão com o chão
    personagem.colisao_chao(chao)

    # Mover o personagem
    personagem.mover(teclas)

    # Preencher a tela com a cor preta
    tela.fill(preto)

    # Desenhar o chão e o personagem
    chao.desenhar(tela)
    pygame.draw.rect(tela, personagem.cor, personagem.rect)

    # Atualizar a tela
    pygame.display.flip()
