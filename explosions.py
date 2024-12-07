from pygame import sprite
from pygame import *

class Explosion(sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.images[]
        for num in range(1,6):
            img = image.load()
            img.transform.scale(img(100,100))
        self.index = 0
        self.image = self.images[self.index]
        self.rect.center = [850,500]
        self.counter = 0
    
    def update(self):
        explosion_speed = 4
        self.counter +1
        if self.counter >= explosion_speed and self.index < len(self.images) -1:
            self.counter = 0
            self.index +=1
            self.images = self.images[self.index]
        if self.index >= len(self.images) -1 and self.counter >= explosion_speed:
            self.kill()