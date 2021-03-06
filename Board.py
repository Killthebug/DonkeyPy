#This defines the very basic building block of the floor and the various levels that this game is made up of

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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-1

    def changeImage(self, newImage):
        self.image = pygame.image.load(newImage)

