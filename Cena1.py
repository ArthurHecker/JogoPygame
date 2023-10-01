import pygame
from personagem import Personagem
from chao import Chao

class Cena1():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.objetos = []
        self.spawn()
        self.player = self.objetos[0]

    def input(self, evento):
        self.player.input(evento)

    def tick(self):
        for objeto in self.objetos:
            objeto.tick()
        for objeto in self.objetos:
            if isinstance(objeto, Personagem):
                for objeto2 in self.objetos:
                    if isinstance(objeto2, Chao):
                        objeto.colisao(objeto2)

    def render(self, screen):
        for objeto in self.objetos:
            objeto.render(screen)

    def spawn(self):
        self.objetos.append(Personagem(100, 0))
        self.objetos.append(Chao(0, 500, self.screen.get_width()))
