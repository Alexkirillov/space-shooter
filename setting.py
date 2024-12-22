from random import randint
class Settings:
    """a class to store all settings for Alien invasion"""
    def __init__(self):

        """initialize the games settings."""
        #Screen setting
        self.screen_whith = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)
        self.ship_speed = 3.5
        self.ship_limit = 3
        #bullet setting
        self.bullet_speed = 4
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (255,255,255)
        self.bullets_allowed = 5
        #Alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 15
        #meteor speed
        #self.meteor_speed = randint(1,4)
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        #how quickly the game speeds up
        self.speedup_scale = 1.1
        #more bullets every round
        self.bullet_scale = 1
        #how quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 3.5
        self.bullet_speed = 4.0
        self.alien_speed = 1.5
        self.alien_points = 50
        self.bullets_allowed = 5

        #fleet_directin of 1 represents right and -1 represents left
        self.fleet_direction = 1
    def increase_speed(self):
        """increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
    
    def more_bullets(self):
        self.bullets_allowed += self.bullet_scale
        self.bullets_allowed = int(self.bullets_allowed + self.bullet_scale)