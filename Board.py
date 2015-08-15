import pygame
import sys
import re
import os
from pygame import *

class Board(pygame.sprite.Sprite):
    """ Defining the board structure now """
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('brick.png')
        self.width = 30
        self.x = x
        self.y = y

    def changeImage(self, newImage):
        self.image = pygame.image.load(newImage)

