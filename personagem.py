import pygame
from cor import *
from Matematicas import colisaoRectRect

class Personagem:
    def __init__(self, x, y, largura = 50, altura= 50, cor = vermelho):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor
        self.velocidade = pygame.Vector2(0,0)
        self.aceleracao = pygame.Vector2(0,0)
        self.gravidade = 1
        self.gravidade = 0
        self.numeroDePulosFeitos = 2
        self.impulso = pygame.Vector2(4,8)
        self.numeroDePulosMaximos = 2
        self.atualizaInfo()

    def atualizaInfo(self):
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = self.rect.width
        self.height = self.rect.height

    def input(self, comando):
        if comando.type == pygame.KEYDOWN:
            if comando.key == pygame.K_LEFT or comando.key == pygame.K_a:
                self.velocidade[0] += -self.impulso[0]
            if comando.key == pygame.K_RIGHT or comando.key == pygame.K_d:
                self.velocidade[0] += self.impulso[0]
            if comando.key == pygame.K_UP or comando.key == pygame.K_w:
                # if self.numeroDePulosFeitos < self.numeroDePulosMaximos:
                #     self.velocidade[1] = -self.impulso[1]
                #     self.numeroDePulosFeitos += 1
                self.velocidade[1] -= self.impulso[1]

            if comando.key == pygame.K_DOWN or comando.key == pygame.K_s:
                pass
                self.velocidade[1] += self.impulso[1]
        if comando.type == pygame.KEYUP:
            if comando.key == pygame.K_LEFT or comando.key == pygame.K_a:
                self.velocidade[0] += self.impulso[0]
            if comando.key == pygame.K_RIGHT or comando.key == pygame.K_d:
                self.velocidade[0] += -self.impulso[0]
            if comando.key == pygame.K_UP or comando.key == pygame.K_w:
                self.velocidade[1] += self.impulso[1]
            if comando.key == pygame.K_DOWN or comando.key == pygame.K_s:
                self.velocidade[1] -= self.impulso[1]
        

    def getPos(self):
        return pygame.Vector2(self.rect.x, self.rect.y)

    def colisao(self, chao):
        resultado = colisaoRectRect(self,chao)
        if resultado[0]:
            if resultado[1].x != 0:
                self.rect.x += resultado[1].x * abs(self.velocidade.x)
                self.aceleracao.x = 0
            if resultado[1].y != 0:
                self.rect.y += resultado[1].y * abs(self.velocidade.y)
                self.aceleracao.y = -self.gravidade
                if resultado[1].y == -1:
                    self.numeroDePulosFeitos = 0

    
    def render(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)
        # desenha o centro do quadrado
        pygame.draw.circle(tela, verde, self.rect.center, 2)
        # mostra a posicao do personagem
        # print(self.rect.x, self.rect.y)

    def tick(self):
            
        # atualiza a posicao x y do personagem
        self.rect.x += self.velocidade[0]
        self.rect.y += self.velocidade[1]+ self.gravidade

        # atualiza a velocidade do personagem
        self.velocidade[0] += self.aceleracao[0]
        self.velocidade[1] += self.aceleracao[1]

        # atualiza a aceleracao do personagem
        self.aceleracao[0] = 0
        # self.aceleracao[1] = self.gravidade
        self.atualizaInfo()