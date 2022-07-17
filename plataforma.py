import pygame
from variables import *
class Ponte(pygame.sprite.Sprite):
    def __init__(self,pos_x):
        pygame.init()
        pygame.mixer.init()
        pygame.sprite.Sprite.__init__(self)
        self.image = chao.subsurface((0,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*7,32*7))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 200
        self.rect.x = pos_x*(32*6.9)
    
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 10
