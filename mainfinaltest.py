# File created by Nathan Cutaran

import pygame as pg
import os 
from settingsfinaltest import *
from spritesfinaltest import *
from random import randint

'''
Things to do:
1) Make platforms go left
2) Figue out jump mechanics
3) Figue out how the player will die
4) How will the colors kill the player
5) Import a bakground
'''

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))

# defines the button perameters, boarder, font, size etc...
def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pg.font.SysFont("Cascadia Code", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pg.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pg.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pg.draw.rect(screen, bg, (x, y, w , h))
    return screen.blit(text_render, (x, y)) 

def menu():
    pg.display.set_caption("menu")
    # creates what is displayed on the buttons
    b0 = button(screen, (10, 10), "Do you wanna play Birdy?", 66, "white on black")
    b1 = button(screen, (WIDTH/3 - 100, HEIGHT/2), "No Thanks", 50, "red on blue")
    b2 = button(screen, (WIDTH/2 + 100, HEIGHT/2), "Let's play", 50, "purple on green")

    # loop of the menu
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # quits pygame
                if b1.collidepoint(pg.mouse.get_pos()):
                    pg.quit()
                elif b2.collidepoint(pg.mouse.get_pos()):
                    g.new()
        pg.display.update()
    pg.quit()

class Game:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.scale_factor = 1.5
        self.win = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.move_speed = 250
        self.bird = Player(self.scale_factor)
