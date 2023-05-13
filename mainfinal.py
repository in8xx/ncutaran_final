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
3) Figure out how the player will die
'''

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

pg.init()
screen = pg.display.set_mode((700, 500))

# defines the button perameters, boarder, font, size etc...
def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pg.font.SysFont("inkfree", size)
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
    b0 = button(screen, (10, 10), "Do you wanna play FlAPPY?", 59, "white on black")
    b1 = button(screen, (150, 300), "Na", 40, "red on blue")
    b2 = button(screen, (450, 300), "Let's play", 40, "purple on green")

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

# create game class in order to pass properties to the sprites file
class Game:
    def __init__(self):
        # instantiates the game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font("inkfree")
        print(self.screen)

    # method that starts a new game
    def new(self):
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for i in range(0,5):
            # calls the variable "m", the mob class
            m = Mob(20,20,(RED))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()

    # method that has the game loop
    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            # calls upon the methods listed below
            self.events()
            self.update()
            self.draw()

    # method for recieving the user input
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.input()

            

    # method for drawing the game

    # Method that draws text, numbers, etc.
    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        self.draw_score(str(self.score), 40 , BLACK, 15, 5)
        self.draw_instructions("Press Space to Start", 40, BLACK, WIDTH/2, 20)

        pg.display.flip()

    # method for drawing the score on the top left
    def draw_score(self, text, size, color, x, y):
        font_name = pg.font.match_font('inkfree')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect) 
    
    # method for drawing the instructions
    def draw_instructions(self, text, size, color, x, y):
        font_name = pg.font.match_font('inkfree')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)  
    
    
    # method that updates the results of player's position when colliding with the mobs
    def update(self):
        # Updates the the sprites in the game loop
        self.all_sprites.update()
        
        # variable for when the mob hits the plater
        mhits = pg.sprite.spritecollide(self.player, self.enemies, False)
        # when mob hits...
        if mhits:
            # mob hits player on the left, then the moves 10 pixels to right
            if self.player.vel.x < 0:
                self.player.pos.x += 10
            
            # mob hits player on the right, then  moves player 10 pixels to the left
            if self.player.vel.x > 0:
                self.player.pos.x -= 10
            # mob hits player from bottom, then moves player 10 pixels up

            if self.player.vel.y > 0:
                self.player.pos.y -= 10

            # mob hits player from the top, then moves player 10 pixels doen
            if self.player.vel.y < 0:
                self.player.pos.y += 10
                

# instantiates the game class
g = Game()

# starts game loop
while g.running:
    menu()
    g.new()

pg.quit()