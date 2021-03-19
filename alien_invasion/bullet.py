import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def _init_(self, ai_game):
        super()._init_()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.sttings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.bullet = pygame.sprite.Group()
        self.y = float(self.rect.y)


    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color,self.rect)