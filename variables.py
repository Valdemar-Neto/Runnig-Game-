import pygame
import os 
from random import choice

pygame.init()
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal,'sons')



LARGURA = 640
ALTURA = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA,ALTURA))

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens,'sprite_sheets.png')).convert_alpha()
nuvem = pygame.image.load(os.path.join(diretorio_imagens,'nuvens.png'))
chao = pygame.image.load(os.path.join(diretorio_imagens,'Ponte.png'))
hidrante = pygame.image.load(os.path.join(diretorio_imagens,"hidrante.png"))
passaro = pygame.image.load(os.path.join(diretorio_imagens,'passaro.png')).convert_alpha()

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons,'colisao.wav'))
som_pontuação = pygame.mixer.Sound(os.path.join(diretorio_sons, 'coin.wav'))
som_pontuação.set_volume(1)


colidiu = False

escolha_obstaculo = choice([0,1])

pontos = 0

velocidae_jogo = 10

background = pygame.image.load(os.path.join(diretorio_imagens,'back.png')).convert()
background = pygame.transform.scale(background,(LARGURA,ALTURA))
relogio = pygame.time.Clock()