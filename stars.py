import pygame
from pygame.sprite import Sprite
from random import randint
random_4 = randint(10,30)
class Star(Sprite):
    """a class to represent a single alien in the fleet"""
    def __init__(self,ai_game):
        """initialize the alien and set its start position"""
        super().__init__()
        self.screen = ai_game.screen
        
        #load the alien image and set its rect attribute.
        """transform.scale method for changing images size"""
        self.image = pygame.transform.scale(pygame.image.load("images/star.png"),(random_4,random_4))
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact horizontal position
        self.x = float(self.rect.x)