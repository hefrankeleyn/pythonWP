#Let all setting put in here
class Settings():
    def __init__(self):
        #init game setting
        
        #screen settings
        self.screen_width = 1366
        self.screen_height = 384
        self.bg_color=(230,230,230)
        
        # ship setting
        self.ship_speed_factor=1.5
        self.ship_limit=3
        
        #bullet setting
        self.bullet_speed_factor=3
        self.bullet_width=300
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3
        
        # alien setting
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        # if fleet_direction is '1' alien move right,else if fleet_direction value is '-1' alien move left
        self.fleet_direction=1 
        
        #speed setting
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """init the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        #when fleet_direction value is 1 move to right
        self.fleet_direction = 1
        
        #make score
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
