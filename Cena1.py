import pygame

# Definir as cores
class Cores:
    def __init__(self):
        self.preto = preto = (0, 0, 0)
        self.branco = branco = (255, 255, 255)
        self.vermelho = vermelho = (255, 0, 0)

# Defina a tela (se for uma janela de jogo, defina aqui)
largura, altura = 1600, 900
tela = pygame.display.set_mode((largura, altura))

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
        self.altura_do_salto = 1
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

