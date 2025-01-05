from pygame import *

class Explosion(sprite.Sprite):
    def __init__(self,enemy_x, enemy_y, anim_dir):
        super().__init__()
        self.images = []
        for num in range(1,6):
            img = image.load(f"animations/{anim_dir}/exp{num}.png")
            img = transform.scale(img,(100,100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [enemy_x,enemy_y]
        self.counter = 0
    
    def update(self):
        explosion_speed = 4
        self.counter +=1
        if self.counter >= explosion_speed and self.index < len(self.images) -1:
            self.counter = 0
            self.index +=1
            self.image = self.images[self.index]
        if self.index >= len(self.images) -1 and self.counter >= explosion_speed:
            self.kill()