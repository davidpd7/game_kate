import pygame

class Hero ():

    def __init__(self):
        
        self.__hero_image = pygame.image.load('images/kate.png')
        self.__hero_image.set_clip(pygame.Rect(0, 0, 64, 128))
        self.image = self.__hero_image.subsurface(self.__hero_image.get_clip())
        self.rect = self.image.get_rect()
        
        self.__frame = 0
        self.__right_states = { 0: (0, 0, 64, 128), 
                                1: (64, 0, 64, 128), 
                                2: (128, 0, 64, 128), 
                                3: (192, 0, 64, 128), 
                                4: (256, 0, 64, 128), 
                                5: (320, 0, 64, 128), 
                                6: (384, 0, 64, 128), 
                                7: (448, 0, 64, 128), 
                                8: (512, 0, 64, 128), 
                                9: (576, 0, 64, 128) }
        self.__left_states = {  0: (0, 128, 64, 128), 
                                1: (64, 128, 64, 128), 
                                2: (128, 128, 64, 128), 
                                3: (192, 128, 64, 128), 
                                4: (256, 128, 64, 128), 
                                5: (320, 128, 64, 128), 
                                6: (384, 128, 64, 128), 
                                7: (448, 128, 64, 128), 
                                8: (512, 128, 64, 128), 
                                9: (576, 128, 64, 128) }
        self.__speed = 6


    def render(self, frame_set):
        self.__frame += 1
        if self.__frame > (len(frame_set)- 1):          
            self.__frame = 1
        return frame_set[self.__frame] 

    def render_rect(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.__hero_image.set_clip(pygame.Rect(self.render(clipped_rect)))

        else:
            self.__hero_image.set_clip(pygame.Rect(clipped_rect))
            
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.render_rect(self.__left_states)
            self.rect.x -= self.__speed
        if direction == 'right':
            self.render_rect(self.__right_states)
            self.rect.x += self.__speed
        
        if direction == 'stand_left':
            self.render_rect(self.__left_states[0])
        if direction == 'stand_right':
            self.render_rect(self.__right_states[0])
      
        self.image = self.__hero_image.subsurface(self.__hero_image.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            quit = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
           