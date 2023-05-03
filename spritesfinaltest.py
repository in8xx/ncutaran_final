# File created by Nathan Cutaran
import pygame as pg

from settingsfinaltest import *
from random import randint
vec = pg.math.Vector2

# creates a player class
class Player(pg.sprite.Sprite):
    def __init__(self, scale_factor):
        pg.sprite.Sprite.__init__(self)
        # properties
        # self.game = game
        self.image = pg.Surface((100,100))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.y_vel=0
        self.gravity = 10
        self.flap_speed = 250
        self.update_on = False


# method in player class that updates the position after clicking the spacebar
    def update(self, dt):
        if self.update_on:
            self.gravity(dt)

            if self.rect.y<=0 and self.flap_speed==250:
                self.rect.y=0
                self.flap_speed=0
                self.y_velocity=0
            elif self.rect.y>0 and self.flap_speed==0:
                self.flap_speed=250

    def gravity(self,dt):
        self.y_velocity+=self.gravity*dt
        self.rect.y+=self.y_velocity

    def flap(self,dt):
        self.y_velocity=-self.flap_speed*dt


# creates a mob class, similar to the player
class Mob(pg.sprite.Sprite):
    def __init__(self,width,height, color):
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01

# method that defines the boundaries for the mob sprites
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric

# no input as this class is for mobs, however we can modify this to collide witht the boundaries and the player
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos

class Pipe:
    def __init__(self,scale_factor,move_speed):
        
        self.pipe_distance=200
        self.rect_up.y=randint(250,520)
        self.rect_up.x=600
        self.rect_down.y=self.rect_up.y-self.pipe_distance-self.rect_up.height
        self.rect_down.x=600
        self.move_speed=move_speed
