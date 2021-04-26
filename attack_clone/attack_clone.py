import sys
from time import sleep

import pygame


from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from blaster import Blaster
from clone import Clone

class AttackClone:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Attack Clone")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.blasters = pygame.sprite.Group()
        self.clones = pygame.sprite.Group()

        self._create_fleet()

        self._play_button = Button(self, "Play")
        
        
    def run_game(self):
        while True:
            self._check_events()
            

            if self.stats.game_active:
                self.ship.update()
                self._update_blasters()
                self._update_clones()

            self._update_screen()    
           

    def _check_events(self):
        for event in pygame.event.get():              
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos) 


    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()

            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            self.clones.empty()
            self.blasters.empty()

            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)
   
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_blaster()
    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_blaster(self):
        if len (self.blasters) < self.settings.blasters_allowed:
            new_blaster = blaster(self)
            self.blasters.add(new_blaster)

    def _update_blasters(self):
        self.blasters.update()
        for blaster in self.blasters.copy():
            if blaster.rect.bottom <= 0:
                self.blasters.remove(blaster)

        self._check_blaster_clone_collisions()
    
    def _check_blaster_clone_collisions(self):
        collisions = pygame.sprite.groupcollide(self.blasters, self.clones, True,True)

        if collisions:
            for clones in collisions.values():
                self.stats.score += self.settings.clone_points * len(clones)
            self.sb.prep_score()
            self.sb.check_high_score()

            
        if not self.clones:
            self.blasters.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            self.stats.level += 1
            self.sb.prep_level()

    def _update_clones(self):

        self._check_fleet_edges()
        self.clones.update()

        if pygame.sprite.spritecollideany(self.ship, self.clones): 
            self._ship_hit()

        self._check_clones_bottom()
    
    def _check_clones_bottom(self):
        screen_rect = self.screen.get_rect()
        for clone in self.clones.sprites():
            if clone.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        if self.stats.ships.left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.clones.empty()
            self.blasters.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Create the fleet of clones."""
        clone= clone(self)  
        clone_width, clone_height = clone.rect.size
        availble_space_x = self.settings.screen_width - (2 * clone_width)
        number_clones_x = availble_space_x // (2 * clone_width)

        ship_height = self.ship.rect.ship_height
        availble_space_y = (self.settings.screen_height - (3 * clone_height) - ship_height)

        number_rows = availble_space_y // (2 * clone_height)

        #create the full fleet of clones.
        for row_number in range(number_rows):
            for clone_number in range(number_clones_x):
                self._create_clone(clone_number, row_number)

    def _create_clone(self, clone_number, row_number):
        clone = clone(self)
        clone_width, clone_height = clone.rect.size
        clone.x = clone_width + 2 * clone_width * clone_number
        clone.rect.x = clone.x
        clone.rect.y = clone.rect.height + 2 * clone.rect.height * row_number
        self.clones.add(clone)

    def _check_fleet_edges(self):
        for clone in self.clones.sprites(): 
            if clone.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for clone in self.clones.sprites():
            clone.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for blaster in self.blasters.sprites():
            blaster.draw_blaster()
        self.clones.draw(self.screen)

        #draw the score information
        self.sb.show_score()

        #draw the sore information
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
        

    
   if __name__ == "__main__":
        
        ai = AttackClones()
        ai.run_game()