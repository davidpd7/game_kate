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

    def __init__(self) -> None:

        pygame.init()
<<<<<<< Updated upstream
        self.screen = pygame.display.set_mode((Game.screen_weight,Game.screen_height))
        pygame.display.set_caption(Game.game_caption)
        pygame.display.set_icon(Game.icon)
=======
        self.screen = pygame.display.set_mode((Game.__screen_weight,Game.__screen_height))
        pygame.display.set_caption(Game.__game_caption)
        pygame.mixer.music.load (os.path.join(*Game.__music_path))
        pygame.display.set_icon(Game.__icon)
>>>>>>> Stashed changes
        self.quit = False
        pygame.mixer.music.play(-1)
        self.fps = 18
        self.clock = pygame.time.Clock()

    def run(self):

        while self.quit == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
<<<<<<< Updated upstream
            self.__render()
=======
            self.render()
>>>>>>> Stashed changes
            self.player.handle_event(event)
            self.clock.tick(self.fps)
        self.__quit_game()
    
    def __render(self):
        print('Hello')
        self.screen.blit(Game.background,(0,0))
        self.screen.blit(Game.player.image, Game.player.rect)
        pygame.display.flip()

<<<<<<< Updated upstream
    def __quit_game(self):
=======
    def render(self):
        self.screen.blit(Game.__background,(0,0))
        self.screen.blit(Game.player.image, Game.player.rect)
        pygame.display.flip()

    def quit_game(self):
                
        pygame.quit()
>>>>>>> Stashed changes

        pygame.quit()