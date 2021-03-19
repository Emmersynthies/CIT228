import sys

import pygame
from pygame.sprite import Sprite
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:

    def _init_(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().screen_width
        self.settings.screen_height = self.screen.get_rect().screen_height
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats

        self.ship = Ship(self)
        self.bullet=pygame.sprite.Group()
        self.alien = pygame.sprite.Group()

        self._create_fleet()
        
        
    def run_game(self):
        while True:
            self._check_events()
            

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()    
           

            pygame.display.flip()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print("Mouse position tuple=",mouse_pos)
                self._check_play_button(mouse_pos) 
                
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
   
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.k_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len (self.bullet) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)

    def _update_bullets(self):
        self.bullet.update()
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)

        self.check_bullet_alien_collision()
    
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullet, self.alien, True,True)

        if not self.alien:
            self.bullet.empty()
            self._create_fleet()

    def _update_aliens(self):

        self._check_fleet_edges()
        self.alien.update()

        if pygame.sprite.spritecollideany(self.ship, self.alien): 
            self._ship_hit()
            self._check_aliens_bottom()
    
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.alien.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        if self.stats.ship.left>0:
            self.stats.ships_left-=1
            self.alien.empty()
            self.bullet.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0,5)
        else:
            self.stats.game_active = False

    def _create_fleet(self):
        alien= Alien(self)  
        alien_width, alien_height = alien.rect.size
        availble_space_x = self.settings_width - (2* alien_width)
        number_aliens_x = availble_space_x // (2* alien_width)

        ship_height = self.ship.rect.ship_height
        availble_space_y = (self.settings.screen_height - (3* alien_height) - ship_height)

        number_rows = availble_space_y // (2* alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
        self.alien.add(alien)

    def _check_fleet_edges(self):
        for alien in self.alien.sprites(): 
            if alien.check_edges():
                self.settings.fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction*= -1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.alien.draw(self.screen)

        pygame.display.flip()
        pygame.display.set_mode() 

    def blitme(self):   
        self.screen.blit(self.msg_image, self.msg_image_rect)





    if _name_ == 'main':
        ai = AlienInvasion()
        ai.run_game()