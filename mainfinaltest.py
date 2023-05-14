# File created by Nathan Cutaran

import pygame as pg
import os 
from settingsfinal import *

from random import randint
import random

'''
Things to do:
1) Make platforms go left
2) Figue out jump mechanics
3) Figure out how the player will die
'''

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# pg.init()
# screen = pg.display.set_mode((WIDTH,HEIGHT))

# # defines the button perameters, boarder, font, size etc...
# def button(screen, position, text, size, colors="white on blue"):
#     fg, bg = colors.split(" on ")
#     font = pg.font.SysFont("inkfree", size)
#     text_render = font.render(text, 1, fg)
#     x, y, w , h = text_render.get_rect()
#     x, y = position
#     pg.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
#     pg.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
#     pg.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
#     pg.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
#     pg.draw.rect(screen, bg, (x, y, w , h))
#     return screen.blit(text_render, (x, y)) 

# def menu():
#     pg.display.set_caption("menu")
#     # creates what is displayed on the buttons
#     b0 = button(screen, (10, 10), "Do you wanna play FlAPPY?", 59, "white on black")
#     b1 = button(screen, (150, 300), "Na", 40, "red on blue")
#     b2 = button(screen, (450, 300), "Let's play", 40, "purple on green")

#     # loop of the menu
#     while True:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#             if event.type == pg.KEYDOWN:
#                 if event.key == pg.K_ESCAPE:
#                     pg.quit()
#             if event.type == pg.MOUSEBUTTONDOWN:
#                 # quits pygame
#                 if b1.collidepoint(pg.mouse.get_pos()):
#                     pg.quit()
#                 elif b2.collidepoint(pg.mouse.get_pos()):
#                     new()
#         pg.display.update()
#     pg.quit()


# create game class in order to pass properties to the sprites file

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption("my game")
score = 0
clock = pg.time.Clock()
running = True
font_name = pg.font.match_font("inkfree, 32")

bird = pg.Surface((50,50))
bird.fill(BLUE)
bird.get_rect()
bird_x = 50
bird_y = HEIGHT/2
bird_change = 0

def birdy(x,y):
    screen.blit(bird, (x,y))

pipe_width = 70
pipe_height = random.randint(200,300)
pipe_color = (255, 215, 0)
pipe_change = -4
pipe_x = 500

def pipes(height):
    pg.draw.rect(screen, pipe_color, (pipe_x, 0, pipe_width, height))
    bottom_pipe_height = 700 - height - 150
    pg.draw.rect(screen, pipe_color, (pipe_x, 700, pipe_width, -bottom_pipe_height))


def pipe_collision(pipe_x, pipe_height, bird_y, bottom_pipe_height):
    if pipe_x >= 50 and pipe_x <= (50 + 64):
        if bird_y <= pipe_height or bird_y >= (bottom_pipe_height - 64):
            return True
        return False



def draw_score(scores):
    display = GAME_FONT.render("score:{scores}", True, (255,255,255))
    screen.blit(display,(10,10))


def start():
    start = GAME_FONT.render("press space bar to start", True, (255,255,255))
    screen.blit(start, (200, 100))
    pg.display.update()

scores_list = [0]

def dead():
    maximum = max(scores_list)
    game_over = GAME_FONT.render("you died!", True, (RED))
    screen.blit(game_over, (300, 300))
    
    high_score = GAME_FONT.render("score: {score} high score: {score}", True, (SLIME))
    screen.blit(high_score, (135, 400))

    play_again = GAME_FONT.render("press space bar to play again", True, (SLIME))
    screen.blit(play_again, (150, 500))

    if score == maximum:
        new_score = GAME_FONT.render("congrats!, new high score", True, (BABYBLUE))
        screen.blit(new_score, (200, 200))
    


running = True

wait = True

collide = False

while running:
    screen.fill(BLACK)

    while wait:
        if collide:
            dead()
            start()

        else:
            start()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    score = 0
                    bird_y = 350
                    pipe_x = 700

                    wait = False
                
            if event.type == pg.QUIT:
                wait = False
                running = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bird_change = -10
        
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                bird_change = 5

    bird_y += bird_change
    birdy(bird_x, bird_y)
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 701:
        bird_y = 701

    pipe_x += pipe_change

    collide = pipe_collision(pipe_x, pipe_height, bird_y, pipe_height + 150)

    if collide:
        scores_list.append(score)
        wait = True

    if pipe_x <= -10:
        pipe_x = 700
        pipe_height = random.randint(100,300)
        score += 1
    pipes(pipe_height)

    pipes(pipe_height)

    birdy(bird_x, bird_y)

    draw_score(scores_list)

    pg.display.update()

pg.quit()



