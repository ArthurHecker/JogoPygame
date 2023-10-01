import pygame
from cor import *

class Personagem:
    def __init__(self, x, y, largura = 50, altura= 50, cor = vermelho):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor
        self.velocidade = [0,0]
        self.aceleracao = [0,0]
        self.gravidade = 0.1
        self.pulando = False

    def input(self, comando):
        if comando.type == pygame.KEYDOWN:
            if comando.key == pygame.K_LEFT or comando.key == pygame.K_a:
                self.velocidade[0] += -1
            if comando.key == pygame.K_RIGHT or comando.key == pygame.K_d:
                self.velocidade[0] += 1
            if comando.key == pygame.K_UP or comando.key == pygame.K_w:
                if not self.pulando:
                    self.aceleracao[1] = -4.4
                    self.pulando = True
            if comando.key == pygame.K_DOWN or comando.key == pygame.K_s:
                pass
        if comando.type == pygame.KEYUP:
            if comando.key == pygame.K_LEFT or comando.key == pygame.K_a:
                self.velocidade[0] += 1
            if comando.key == pygame.K_RIGHT or comando.key == pygame.K_d:
                self.velocidade[0] += -1
            if comando.key == pygame.K_UP or comando.key == pygame.K_w:
                pass
            if comando.key == pygame.K_DOWN or comando.key == pygame.K_s:
                pass
        

    def colisao(self, chao):
        if chao.rect.colliderect(self.rect):
            self.rect.y = chao.rect.y - self.rect.height
            self.velocidade[1] = 0
            self.pulando = False
    
    def render(self, screen):
        pygame.draw.rect(screen, self.cor, self.rect)

    def tick(self):
            
        # atualiza a posicao x y do personagem
        self.rect.x += self.velocidade[0]
        self.rect.y += self.velocidade[1]

        # atualiza a velocidade do personagem
        self.velocidade[0] += self.aceleracao[0]
        self.velocidade[1] += self.aceleracao[1]

        # atualiza a aceleracao do personagem
        self.aceleracao[0] = 0
        self.aceleracao[1] = self.gravidade