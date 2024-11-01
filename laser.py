import random 
import arcade 
from settings import *

class Bullet(arcade.Sprite):

    def __init__(self, filename, sprite_scaling, speed):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = speed

    def update(self):
        # Move the bullet
        self.center_x += self.change_x
        self.center_y += self.change_y

        

