import pygame.sprite
import os 
from random import randrange, choice
from variables import *

class Corredor(pygame.sprite.Sprite):

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'jump.wav'))
        self.som_pulo.set_volume(1)
        self.imagens_corredor = []
        for i in range(9):
            img = sprite_sheet.subsurface((i*183,0),(183,205))
            img = pygame.transform.scale(img, (183/2.3,205/2.3))
            self.imagens_corredor.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_corredor[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = ALTURA - 103 - 87//2
        self.rect.center = (100,ALTURA-103)
        self.pulo = False
    
    def pular(self):
        self.pulo = True
        self.som_pulo.play()


    def update(self):
        if self.pulo == True:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -=20 
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial
        if self.index_lista >8:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_corredor[int(self.index_lista)]
    

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
