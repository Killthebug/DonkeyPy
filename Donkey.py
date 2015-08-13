import pygame
import os
import sys
import Person
from pygame import *
from Person import *

class Donkey(Person):
    """ Child Class of Person , defined the Protagonist """
    def __init__(self):
        self.player = pygame.image.load('donkey.png')
        self.x = 30
        self.y = 538
        self.lives = 3
        self.coins = 0
        self.body = pygame.image.load('donkey_left.png')
        self.x_Change = 0
        self.y_Change = 0

    def moveLeft(self):
        self.x_Change = -5
        self.x = self.x + self.x_Change
        self.body = pygame.image.load('donkey_left.png')

    def moveRight(self):
        self.x_Change = 5
        self.x = self.x + self.x_Change
        self.body = pygame.image.load('donkey.png')

    def playerDead(self):
        self.lives -= 1

    def collectCoin(self):
        self.coins += 1

    def x_Stop(self):
        self.x -= self.x_Change
        
    def y_Stop(self):    
        self.y += self.y_Change
