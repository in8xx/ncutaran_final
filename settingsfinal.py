import pygame as pg
pg.init()

# Game Parameters
WIDTH = 700
HEIGHT = 700
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3
GAME_FONT = pg.font.SysFont("inkfree", 32, False, False)


# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
BABYBLUE = (137, 207, 240)
SLIME = (50, 205, 50)
RED = (255,50,50)

# defines a random color
from random import randint
RANDCOLOR = [randint(0,255), randint(0,255), randint(0,255)]

FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False
