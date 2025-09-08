import sys
import pygame
from random import randint
from time import sleep


def reset_bola():
    bola.center = (LARGURA_TELA // 2, ALTURA_TELA // 2)
    barra_direita.y = (ALTURA_TELA - ALTURA_BARRA)// 2
    barra_esquerda.y = (ALTURA_TELA - ALTURA_BARRA)// 2
   

(LARGURA_TELA), ALTURA_TELA = 800, 600
FPS = 60
BRANCO = (255,255,255)
PRETO = (0,0,0)


LARGURA_BARRA, ALTURA_BARRA = 10, 100
VELOCIDADE_BARRA = 7


TAMANHO_BOLA = 20
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5

pygame.init()
tela = pygame.display.set_mode(((LARGURA_TELA), ALTURA_TELA))
pygame.display.set_caption("pong turma 1")
clock = pygame.time.Clock()
temporizador = 0

barra_esquerda = pygame.Rect(10, (ALTURA_TELA - ALTURA_BARRA) // 2, LARGURA_BARRA, ALTURA_BARRA)
barra_direita = pygame.Rect((LARGURA_TELA) - 20, (ALTURA_TELA - ALTURA_BARRA) // 2, LARGURA_BARRA, ALTURA_BARRA)
bola = pygame.Rect(((LARGURA_TELA) - TAMANHO_BOLA) // 2, (ALTURA_TELA - TAMANHO_BOLA) // 2, TAMANHO_BOLA, TAMANHO_BOLA)

velocidade_esquerda = 0
velociade_direita = 0

if randint(1,2) == 1:
    velocidade_bola_x = VELOCIDADE_BOLA_X
else:
    velocidade_bola_x = -VELOCIDADE_BOLA_X

if randint(0,1) == 0:
    velocidade_bola_y = VELOCIDADE_BOLA_Y
else:
    velocidade_bola_y = -VELOCIDADE_BOLA_Y

placar_esquerda = 0
placar_direita = 0
placar_fonte = pygame.font.Font(None, 36)


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                velocidade_esquerda = -VELOCIDADE_BARRA
            if evento.key == pygame.K_s:
                velocidade_esquerda = VELOCIDADE_BARRA
            if evento.key == pygame.K_UP:
                velociade_direita = -VELOCIDADE_BARRA
            if evento.key == pygame.K_DOWN:
                velociade_direita = VELOCIDADE_BARRA
            
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w or evento.key == pygame.K_s:
                velocidade_esquerda = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                velociade_direita = 0

    barra_esquerda.y += velocidade_esquerda
    barra_direita.y += velociade_direita

    barra_esquerda.y = max(0, min(ALTURA_TELA - ALTURA_BARRA,barra_esquerda.y))
    barra_direita.y = max(0,min(ALTURA_TELA - ALTURA_BARRA,barra_direita.y))


    bola.x += velocidade_bola_x
    bola.y += velocidade_bola_y

    if bola.top <= 0 or bola.bottom >= ALTURA_TELA:
        velocidade_bola_y = -velocidade_bola_y

    if bola.colliderect(barra_esquerda) or bola.colliderect(barra_direita):
        velocidade_bola_x = -velocidade_bola_x

    if bola.left <= 0:
        placar_direita += 1
        velocidade_bola_x = -velocidade_bola_x
        reset_bola()
        temporizador = 1

    
    if bola.right >= LARGURA_TELA:
        placar_esquerda += 1
        velocidade_bola_x = -velocidade_bola_x
        reset_bola()
        temporizador = 1

    tela.fill(PRETO)
    pygame.draw.rect(tela, (30,144,255), barra_esquerda)
    pygame.draw.rect(tela, (178,34,34), barra_direita)
    pygame.draw.rect(tela, BRANCO, bola)
    pygame.draw.aaline(tela, BRANCO, (LARGURA_TELA // 2, 0),(LARGURA_TELA // 2, ALTURA_TELA))
 
    texto_esquerda = placar_fonte.render(str(placar_esquerda),True,BRANCO)
    texto_direita = placar_fonte.render(str(placar_direita),True,BRANCO)
    tela.blit(texto_esquerda, (LARGURA_TELA // 4 - texto_esquerda.get_width() // 2, 20))
    tela.blit(texto_direita, (3 * LARGURA_TELA // 4 - texto_direita.get_width() // 2,20))


    pygame.display.flip()
    if temporizador == 1:
        sleep(2)
        temporizador = 0
    clock.tick(FPS)

pygame.quit()