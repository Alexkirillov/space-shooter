import pygame
from pygame.sprite import Sprite

class Boss(Sprite):
    """a class for the boss"""
    def __init__(self,ai_game):
        """initialize boss start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.direction = True
        #bosses correct size.
        """transform.scale method for changing images size"""
        self.image = pygame.transform.scale(pygame.image.load("images/boss.png"),(280,150))
        self.rect = self.image.get_rect()
        self.boss_hp = 50
        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        print(self.rect.x,self.rect.y)
        #store the aliens exact horizontal position
        self.x = float(self.rect.x)
        self.boss_speed = 2.0
    def check_edges(self):
        """return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """move the alien to the right or left."""
        #self.x += self.settings.alien_speed
        if self.rect.x <= 0:
            self.boss_speed = -2.0
            print("movement to the right",self.boss_speed)
            #self.direction = True
        elif self.rect.x >= 1500: #! problem 1
            self.boss_speed = 2.0
            print("movement to the left",self.boss_speed)
        print("movement",self.boss_speed)
        print(self.rect.x,"this is the x coordinate")

        self.x += self.boss_speed * self.settings.fleet_direction
        self.rect.x = self.x
    