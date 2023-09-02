import pygame
from player import Hero
import os

class Game():

    __screen_weight = 720
    __screen_height = 480
    __game_caption = "Actividad"  
    __icon_path = ['images', 'icono.png']
    __icon = pygame.image.load(os.path.join(*__icon_path))
    __background_path = ['images', 'fondo.png']
    __background = pygame.image.load(os.path.join(*__background_path))
    __music_path = ['music', 'ambiente.ogg']
    player = Hero()

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((Game.__screen_weight,Game.__screen_height))
        pygame.mixer.music.load(os.path.join(*Game.__music_path))
        pygame.mixer.music.play(-1)
        self.quit = False
        self.fps = 18
        self.clock = pygame.time.Clock()

    def run(self):

        while self.quit == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
            self.__render()
            self.display()
            
            self.player.handle_event(event)
            self.clock.tick(self.fps)
        self.__quit_game()
    
    def display(self):
        pygame.display.set_caption(Game.__game_caption)
        pygame.display.set_icon(Game.__icon)

    def __render(self):
        self.screen.blit(Game.__background,(0,0))
        self.screen.blit(Game.player.image, Game.player.rect)
        print(Game.player.rect)
        pygame.display.flip()

    def __quit_game(self):
                
        pygame.quit()