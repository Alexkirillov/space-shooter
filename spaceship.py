import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """A class to manag the ship."""

    def __init__(self,ai_game):
        super().__init__()
        """initialize the ship and set is to starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load te ship image and get its rect
        self.image = pygame.image.load("images\spaceship_1.png")
        self.rect = self.image.get_rect()

        #start each new ship at the botom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for ships exact horizontal position
        self.x = float(self.rect.x)
        # flag; start with a ship thats not moving
        self.moving_right = False
        self.moving_left =False
        """update the ships position based on the movement flag"""
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect object from self.x.
        self.rect.x = self.x
    
    def center_ship(self):
        """center the ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)