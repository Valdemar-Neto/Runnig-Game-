import pygame
from variables import *
from random import randrange, choice

class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.sprite.Sprite.__init__(self)
        self.image = nuvem.subsurface((0,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*3,32*3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(10,200,50)
        self.rect.x = LARGURA - randrange(30,300,90)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(10,200,50)
        self.rect.x -= velocidae_jogo

