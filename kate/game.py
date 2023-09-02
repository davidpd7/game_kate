import pygame
from player import Hero
import os

class Game():

    screen_weight = 720
    screen_height = 480
    game_caption = "Actividad"  
    icon_path = ['images', 'icono.png']
    icon = pygame.image.load(os.path.join(*icon_path))
    background_path = ['images', 'fondo.png']
    background = pygame.image.load(os.path.join(*background_path))
    music_path = ['music', 'ambiente.ogg']
    music = pygame.mixer.music.load (os.path.join(*music_path))
    player = Hero()

    def __init__(self) -> None:

        pygame.init()
        self.screen = pygame.display.set_mode((Game.screen_weight,Game.screen_height))
        pygame.display.set_caption(Game.game_caption)
        pygame.display.set_icon(Game.icon)
        self.quit = False
        pygame.mixer.music.play(-1)
        self.fps = 18
        self.clock = pygame.time.Clock()

    def run(self):

        while self.quit == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
            self.__render()
            self.player.handle_event(event)
            self.clock.tick(self.fps)
        self.__quit_game()
    
    def __render(self):
        print('Hello')
        self.screen.blit(Game.background,(0,0))
        self.screen.blit(Game.player.image, Game.player.rect)
        pygame.display.flip()

    def __quit_game(self):

        pygame.quit()