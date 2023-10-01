import pygame
import sys
from cena1 import Cena1
from menu import Menu
from cor import *

class Main():

    def __init__(self) -> None:
        pygame.init()
        largura, altura = 1600*0.7, 900*0.7
        self.screen = pygame.display.set_mode((largura, altura))
        self.cenas = [Menu(self.screen),Cena1(self.screen)]
        self.cenaAtual = 1
        self.run()

    def run(self):
        # Loop principal do jogo
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.cenas[self.cenaAtual].input(evento)

            self.tick() # todo o processamento da logica do jogo
            self.render()   # todo o processamento de desenho
             

    def tick(self):
        self.cenas[self.cenaAtual].tick()

    def render(self):
        # Preencher a tela com a cor preta
        self.screen.fill((0,0,0))
        self.cenas[self.cenaAtual].render(self.screen)
        pygame.display.flip()


Main()