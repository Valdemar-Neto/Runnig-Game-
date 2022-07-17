import pygame
from variables import *

class Obj1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.sprite.Sprite.__init__(self)
        self.image = hidrante.subsurface((0,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*1.75,32*1.8))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center=(LARGURA, ALTURA-90)
        self.rect.x = LARGURA
    
    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= velocidae_jogo
