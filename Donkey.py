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
        self.lives = 5
        self.score = 0
        self.body = pygame.image.load('donkey_left.png')
        self.x_Change = 0
        self.y_Change = 0
        self.canJump = True
        self.rect = self.body.get_rect()
        self.canMoveSide = True
        self.canClimbUp = False
        self.canClimbDown = False
        self.win = False
    
    def resetPos(self):
        self.x = 30
        self.y = 538
        self.update()
    
    def newGame(self):
        self.resetPos()
        self.lives = 5

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

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
        self.y_Change = 0

    def cannotClimb():
        self.canClimbUp = False
        self.canClimbDown = False
   
    def Penalize(self):
        if self.score < 25:
            self.score = 0
        else:
            self.score -= 25

    def Jump(self):
        self.y -= 0.1

    def moveUp(self):
        self.y_Change = 5
        self.y = self.y - self.y_Change
        self.body = pygame.image.load('donkey_ass.png')

    def moveDown(self):
        self.y_Change = -5
        self.y = self.y - self.y_Change
        self.body = pygame.image.load('donkey_ass.png')
