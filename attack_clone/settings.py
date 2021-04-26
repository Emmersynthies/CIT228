class Settings:

    def _init_(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (130, 200, 130)

       
        self.ship_limit = 3

        self.blaster_width = 2
        self.blaster_height = 12
        self.blaster_color = (40, 40, 40)
        self.blaster_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initalize_dynamic_settings()

    def initalize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.blaster_speed= 3.0
        self.clone_speed = 1.0    
 
       self.fleet_direction = 1

       self.clone_points = 45
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.blaster_speed *= self.speedup_scale
        self.clone_speed *= self.speedup_scale

        self.clone_points = int(self.clone_points * self.score_scale)