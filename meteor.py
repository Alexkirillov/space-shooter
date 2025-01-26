from random import randint, random

import pygame
from pygame.sprite import Sprite

class Meteor(Sprite):
    """a class to represent a single alien in the fleet"""
    def __init__(self,ai_game):

        """initialize the alien and set its start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.speed = random() + randint(1,2)
        #load the alien image and set its rect attribute.
        """transform.scale method for changing images size"""
        self.image = pygame.transform.scale(pygame.image.load("images/exp1.png"),(100,100))
        self.rect = self.image.get_rect()

        #store the aliens exact horizontal position
        self.x = float(self.rect.x)
    def update(self):
        """move the alien to the right or left."""
        #self.x += self.settings.alien_speed
        self.rect.y += self.speed
        if self.rect.y >= self.settings.screen_height:
            self.kill()

            
     