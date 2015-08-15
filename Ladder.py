import pygame
import os
import sys
from pygame import *

class Ladder(pygame.sprite.Sprite):
    """ Defines a ladder """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.body = pygame.image.load('ladder.png')
        self.x = 200
        self.y = 110
        self.broken = False

    def breakLadder(self):
        self.body = pygame.image.load('broken.png')
        self.broken = True

    def makeLadder(self):
        self.broken = False


