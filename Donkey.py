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
        self.y = 388
        self.lives = 3
        self.coins = 0
        self.body = pygame.image.load('donkey_left.png')
        self.x_Change = 0
        self.y_Chamge = 0

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

    def stop(self):
        self.x -= self.x_Change

