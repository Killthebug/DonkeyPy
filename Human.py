import pygame
import os
import sys
import Person
import random
from pygame import *
from Person import *

class Human(Person):
    """ Child Class of Person, defined the Villian """
    def __init__(self):
        self.player = pygame.image.load('human.png')
        self.x = 140
        self.y = 50
        self.x_Change = 0
        self.y_Change = 0
        self.direction = 0

    def moveLeft(self):
        self.x_Change = -2
        self.x = self.x + self.x_Change

    def moveRight(self):
        self.x_Change = 2
        self.x = self.x + self.x_Change

    def stop(self):
        self.x -= self.x_Change

    def Update(self, x1, x2):
        self.direction = random.randrange(-1,2)
        if self.direction < 0:
            self.moveLeft()
        else:
            self.moveRight()
        if self.x >= x1 and self.x <= x2:
            pass
        else:
            self.stop()
