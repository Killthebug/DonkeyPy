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

    def moveLeft(self):
        self.x_Change = -3
        self.x = self.x + self.x_Change

    def moveRight(self):
        self.x_Change = 3
        self.x = self.x + self.x_Change

    def stop(self):
        self.x -= self.x_Change

    def randomMove(self):
        return random.randrange(-1,2)

