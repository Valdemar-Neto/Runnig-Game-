from imp import reload
from operator import truediv
from tkinter import font, image_names
from zipfile import LargeZipFile
import pygame
from pygame.locals import *
from sys import exit
import os 
from random import randrange, choice
from variables import *
from corredor import Corredor
from ceu import Nuvens
from plataforma import Ponte
from obstaculo1 import Obj1
from obstaculo2 import Obj2
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Running")

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont("comicsansms", tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def reiniciar():
    global pontos, velocidae_jogo, colidiu, escolha_obstaculo
    pontos = 0
    velocidae_jogo = 10
    colidiu = False
    corredor.rect.y = ALTURA - 103 - 87//2
    corredor.pulo = False
    hydrante.rect.x = LARGURA
    bird.rect.x = LARGURA
    escolha_obstaculo = choice([0,1])


todas_as_sprites = pygame.sprite.Group()

for i in range(4):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

for i in range(4):
    ponte = Ponte(i)
    todas_as_sprites.add(ponte) 

hydrante = Obj1()
todas_as_sprites.add(hydrante)

bird = Obj2()
todas_as_sprites.add(bird)



grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(hydrante)
grupo_obstaculos.add(bird)
corredor = Corredor()
todas_as_sprites.add(corredor)

while True:
    relogio.tick(30)
    tela.fill(BRANCO)

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and colidiu == False:
                    if corredor.rect.y != corredor.pos_y_inicial:
                        pass
                    else:
                        corredor.pular()
                if event.key == K_r and colidiu == True:
                    reiniciar()

    colisoes = pygame.sprite.spritecollide(corredor, grupo_obstaculos, False, pygame.sprite.collide_mask)
    
    tela.blit(background,(0,0))
    todas_as_sprites.draw(tela)

    if hydrante.rect.topright[0]<=0 or bird.rect.topright[0]<=0:
        escolha_obstaculo = choice([0,1])
        hydrante.rect.x = LARGURA
        bird.rect.x = LARGURA
        hydrante.escolha = escolha_obstaculo
        bird.escolha = escolha_obstaculo

    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True
    
    if colidiu == True:
        if pontos % 100 ==0:
            pontos +=1
        game_over = exibe_mensagem("GAME OVER", 45, (255,255,255))
        tela.blit(game_over,(LARGURA//1.8,ALTURA//2.4))
        restart = exibe_mensagem('Pressione r para reiniciar', 20,(255,255,255))
        tela.blit(restart,(LARGURA//1.8, (ALTURA//2)+10))


    else: 
        pontos +=1
        todas_as_sprites.update()
        texto_pontos = exibe_mensagem(pontos, 35, (255,255,255))
    
    if pontos%100 == 0:
        som_pontuação.play()
        if velocidae_jogo >= 23:
            velocidae_jogo +=0
        else:
            velocidae_jogo +=1
    tela.blit(texto_pontos,(520,30))

    pygame.display.flip()