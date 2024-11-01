import os

import arcade

PATH_FOR_ASSETS = os.getcwd() + '/assets'

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ALIEN = 0.2
SPRITE_SCALING_LASER = 0.8
ALIEN_COUNT = 500

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5

PATH_TO_MYSHIP = PATH_FOR_ASSETS+"/space_shooter/PNG/playerShip1_blue.png"
PATH_TO_ALIEN  = PATH_FOR_ASSETS+"/space_shooter/PNG/Enemies/enemyRed1.png"
PATH_TO_BULLET = PATH_FOR_ASSETS+"/space_shooter/PNG/Lasers/laserRed01.png"
sound = arcade.load_sound(PATH_FOR_ASSETS+"/space_shooter/bonus/sfx_laser1.ogg")
fastsound = arcade.load_sound(PATH_FOR_ASSETS+"/space_shooter/bonus/sfx_laser2.ogg")

