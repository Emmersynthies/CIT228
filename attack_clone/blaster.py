import pygame
from pygame.sprite import Sprite

class Blaster(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.blaster_color
        
        self.rect = pygame.Rect(0, 0, self.settings.blaster_width, self.settings.blaster_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        self.y = float(self.rect.y)


    def update(self):
        self.y -= self.settings.blaster_speed
        self.rect.y = self.y

    def draw_blaster(self):
        pygame.draw.rect(self.screen, self.color, self.rect)