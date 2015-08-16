import pygame
import os
import sys
import Person
from pygame import *
from Person import *

class Donkey(Person,pygame.sprite.Sprite):
    """ Child Class of Person , defined the Protagonist """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('donkey.png')
        self.rect = self.image.get_rect()
        self.x = 30
        self.y = 538
        self.rect.x = 30
        self.rect.y = 538
        self.lives = 3
        self.coins = 0
        self.body = pygame.image.load('donkey_left.png')
        self.x_Change = 0
        self.y_Change = 0
        self.rect = self.body.get_rect()
        self.canMoveSide = True
        self.canClimbUp = False
        self.canClimbDown = False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y+3
    
    def calc_Gravity(self):
            self.y_Change = -1
            self.y -= self.y_Change

    def moveLeft(self):
        self.x_Change = -5
        self.x = self.x + self.x_Change
        self.canMoveSide = False
        self.body = pygame.image.load('donkey_left.png')

    def moveRight(self):
        self.x_Change = 5
        self.x = self.x + self.x_Change
        self.canMoveSide = False
        self.body = pygame.image.load('donkey.png')

    def playerDead(self):
        self.lives -= 1

    def collectCoin(self):
        self.coins += 1

    def x_Stop(self):
        self.x -= self.x_Change
        
    def y_Stop(self):    
        self.y += self.y_Change

    def cannotClimb():
        self.canClimbUp = False
        self.canClimbDown = False

    def moveUp(self):
        self.y_Change = 5
        self.y = self.y - self.y_Change
        self.body = pygame.image.load('donkey_ass.png')

    def moveDown(self):
        self.y_Change = -5
        self.y = self.y - self.y_Change
        self.body = pygame.image.load('donkey_ass.png')
