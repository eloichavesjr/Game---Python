import pygame
from random import randint
pygame.init()

x = 350
y = 300

pos_x = 220
pos_y = 800

pos_y_a = 800
pos_y_c = 800

velocidade_outros = 12
velocidade = 10

fundo = pygame.image.load('imagens/tela.jpg')
carro = pygame.image.load('imagens/carro.png')
carro2 = pygame.image.load('imagens/carro2.png')
carro3 = pygame.image.load('imagens/carro3.png')
carro1 = pygame.image.load('imagens/carro1.png')


janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Criando um Jogo com Python")

janela_aberta = True
while janela_aberta:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade    
    if comandos[pygame.K_RIGHT] and x<= 500:
        x+= velocidade    
    if comandos[pygame.K_LEFT] and x>= 200:
        x-= velocidade

        # Colisão
    if ((x + 80 > pos_x and y + 180 > pos_y)):
        y = 1200   

    if (pos_y <= -200):
        pos_y = randint(800, 1000)

    if ((pos_y_a <= -200)):
        pos_y_a = randint(1200, 2000)

    if ((pos_y_c <= -180)):        
        pos_y_c = randint(2200, 3000)

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros + 2
    pos_y_c -= velocidade_outros + 10

    janela.blit(fundo, (0,0)) 
    janela.blit(carro, (x,y))
    janela.blit(carro2, (pos_x,pos_y)) 
    janela.blit(carro3, (pos_x + 150,pos_y_a))
    janela.blit(carro1, (pos_x + 250,pos_y_c))


    #pygame.draw.circle(janela, (0,255,0), (x, y), 50)
    pygame.display.update()

pygame.quit()            
