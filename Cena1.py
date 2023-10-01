import pygame
from personagem import Personagem
from caixa import Caixa

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
                    if isinstance(objeto2, Caixa):
                        objeto.colisao(objeto2)


    def render(self, tela):
        for objeto in self.objetos:
            objeto.render(tela)

    def spawn(self):
        self.objetos.append(Personagem(100, 0))
        self.objetos.append(Caixa(150, 500, self.screen.get_width()/2,200, jogador=self.objetos[0]))
        self.objetos.append(Caixa(360, 10, 20, self.screen.get_height(), jogador=self.objetos[0]))
