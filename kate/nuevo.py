import pygame
from player import Hero

class Game():
    def __init__(self):
        self.screen_weight = 720
        self.screen_height = 480
        pygame.mixer.music.load ('music/ambiente.ogg')
        pygame.mixer.music.play(-1)
        self.player = Hero()
        self.player = self.player((self.screen_weight/2, self.screen_height/1.35))
        self.screen = pygame.display.set_mode((self.screen_weight, self.screen_height))
        pygame.display.set_caption("Actividad")
        self.clock = pygame.time.Clock
        self.icon = pygame.image.load('images/icono.png')
        self.background = pygame.image.load('images/fondo.png')
        self.quit = False
        self.fps = 18

    def running(self):
        while self.quit == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
            self.player.handle_event(event)
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.player.image, self.player.rect)
            self.pygame.display.flip()
            pygame.display.set_icon(self.icon)
            self.clock.tick(self.fps)

def main ():
    pygame.init()
    game = Game()
    game.running()

main()
 

