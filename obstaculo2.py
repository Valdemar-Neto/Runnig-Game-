import pygame
from variables import *
class Obj2(pygame.sprite.Sprite):
    pygame.init()
    pygame.mixer.init()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagem_passaro = []
        for i in range(8):
            img = passaro.subsurface((i*32,0),(32,27))
            img = pygame.transform.scale(img, (32*4,27*4))
            self.imagem_passaro.append(img)
        self.index_lista=0
        self.image = self.imagem_passaro[self.index_lista]
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA,275)
        self.rect.x = LARGURA

    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= velocidae_jogo

            if self.index_lista >7:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.imagem_passaro[int(self.index_lista)]
