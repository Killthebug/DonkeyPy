#Class FireBall that defines the fireballs given out by the Donkey

import pygame
import sys
import os
import time
import time
from pygame import *

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load('fire.png')
       self.rect = self.image.get_rect()
       self.x = x
       self.y = y
       self.level = 5
       self.x_Change = 0
       self.y_Change = 0
       self.canFallDown = False
       self.rect.x = self.x
       self.rect.y = self.y
       self.direction = 0

    def moveLeft(self):
        self.x_Change = -3
        self.x += self.x_Change
        self.rect.x = self.x
    
    def moveRight(self):
        self.x_Change = 3
        self.x += self.x_Change
        self.rect.x = self.x

    def moveDown(self):
        self.y_Change = 5
        self.y += self.y_Change
        self.rect.y = self.y

    def stop(self):
        self.x -= self.x_Change

    def find_Level(self):
        if self.y <= 120:
            self.level = 5
        elif self.y <= 220:
            self.level = 4
        elif self.y <= 320:
            self.level = 3
        elif self.y <= 470:
            self.level = 2
        else:
            self.level = 1

    def shake_It(self, x1, x2):
        if self.x > x1 and self.x < x2:
            if self.direction == 0:
                self.moveRight()
            else:
                self.moveLeft()        
        if self.x - x1 < 50:
            self.direction = 0
        if x2 - self.x < 80:
            self.direction = 1
        if self.x >= x1 and self.x <= x2:
            pass
        else:
            self.stop()

    def moveWeird(self):
        if self.level == 1:
            x1 = -99999999
            x2 = 999999999
        elif self.level == 2:
            x1 = 100
            x2 = 1000
        elif self.level == 3:
            x1 = 300
            x2 = 1170
        elif self.level == 4:
            x1 = 30
            x2 = 900
        else:
            x1 = 150
            x2 = 650
        self.shake_It(x1, x2)
    
