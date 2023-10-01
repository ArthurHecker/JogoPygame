import pygame
import sys
from cena1 import Cena1
from menu import Menu
from cor import *
import time
from threading import Thread


class Main():

    def __init__(self) -> None:
        Thread.__init__(self)
        pygame.init()

        # Definir as dimensões da janela
        dimensoes = pygame.display.get_desktop_sizes()[0]
        self.WINDOW_WIDTH = dimensoes[0] * 0.7
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = dimensoes[1] * 0.7
        self.WINDOW_HEIGHT = 800
        self.FPS_PADRAO = 60.0
        self.UPDATE_CAP = 1.0/self.FPS_PADRAO

        # Criar a janela
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.RESIZABLE)
        self.cenas = [Menu(self.screen),Cena1(self.screen)]
        self.cenaAtual = 1
        pygame.display.set_caption("JOGO DO ARTHUR") # titulo da janela
        Thread(self.run())

    def run(self):
        self.running = True
        render = False
        firstTime = 0
        lastTime = time.time()  # retorna o tempo atual em segundos
        passedTime = 0
        unprocessedTime = 0
        frameTime = 0
        frames = 0
        fps = 0

        while self.running:
                render = False
                firstTime = time.time()
                passedTime = firstTime - lastTime   # tempo que passou desde a ultima vez que o loop foi executado
                lastTime = firstTime            # atualiza o tempo da ultima vez que o loop foi executado

                unprocessedTime += passedTime  # tempo nao processado
                frameTime += passedTime

                # enquanto nao processou td q deveria (devido a lag em render ou coisas assim)
                while unprocessedTime >= self.UPDATE_CAP:
                    # Isso garante que o tempo de atualizacao seja constante
                    # e nao dependa do tempo de renderizacao. Igualando o 
                    # jogo para todos os computadores, apenas aumentando o
                    # fps para computadores mais potentes
                    unprocessedTime -= self.UPDATE_CAP  # Tempo comido
                    render = True

                    self.tick()

                    if frameTime >= 1.0:
                            frameTime = 0
                            fps = frames
                            frames = 0
                            # print("FPS: " + str(fps))

                # Depois de processar o tempo, renderiza
                if render:
                    self.render()
                    frames += 1
                else:
                    time.sleep(0.001)
             

    def tick(self):
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.cenas[self.cenaAtual].input(evento)
        self.cenas[self.cenaAtual].tick()

    def render(self):
        # Preencher a tela com a cor preta
        self.screen.fill(preto)
        self.cenas[self.cenaAtual].render(self.screen)
        pygame.display.flip()


Main()