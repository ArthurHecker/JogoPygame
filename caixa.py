import pygame
from cor import *

class Caixa():
    def __init__(self, x, y, largura, altura = 20, cor = branco, jogador = None):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor
        self.jogador = jogador
        if jogador != None:
            self.retanguloColisor = pygame.Rect(self.rect.x-0.5*jogador.width, self.rect.y -0.5*jogador.width, self.rect.width+ jogador.width, self.rect.height + jogador.height)
    
        self.atualizaInfo()

    def atualizaInfo(self):
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = self.rect.width
        self.height = self.rect.height

    def render(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

        # debug
        # desenha o centro do quadrado
        pygame.draw.circle(tela, verde, self.rect.center, 5)
        if self.jogador != None:
            pygame.draw.rect(tela, (255,255,0), self.retanguloColisor, 1)

    def tick(self):
        self.atualizaInfo()

    def get_rect(self):
        return self.rect