import pygame
from cor import *

class Chao():
    def __init__(self, x, y, largura, altura = 20, cor = branco):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor

    def render(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

    def tick(self):
        pass

    def get_rect(self):
        return self.rect