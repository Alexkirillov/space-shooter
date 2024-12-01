import pygame
from pygame.sprite import Sprite

class Meteor(Sprite):
    """a class to represent a single alien in the fleet"""
    def __init__(self,ai_game):

        """initialize the alien and set its start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #load the alien image and set its rect attribute.
        """transform.scale method for changing images size"""
        self.image = pygame.transform.scale(pygame.image.load("images/alien_ship_python.png"),(120,120))
        self.rect = self.image.get_rect()

        #store the aliens exact horizontal position
        self.x = float(self.rect.x)
    def update(self):
        """move the alien to the right or left."""
        #self.x += self.settings.alien_speed
        self.y += self.settings.meteor_speed
        self.rect.y = self.y