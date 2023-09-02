import pygame
from player import Hero


pygame.init()


screen_weight = 720
screen_height = 480
screen = pygame.display.set_mode((screen_weight,screen_height))
pygame.display.set_caption("Actividad")
clock = pygame.time.Clock()
player = Hero()
icon = pygame.image.load('images/icono.png')
background = pygame.image.load('images/fondo.png')
quit = False
pygame.mixer.music.load ('music/ambiente.ogg')
pygame.mixer.music.play(-1)
fps = 18


while quit == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
    player.handle_event(event)
    screen.blit(background,(0,0))
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    pygame.display.set_icon(icon)
    clock.tick(fps)
        
pygame.quit ()


