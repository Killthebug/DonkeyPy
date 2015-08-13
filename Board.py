import pygame
import sys
import re
import os
from pygame import *

class Board():
    """ Defining the board structure now """
    def __init__(self):
        self.image = pygame.image.load('brick.png')
        self.width = 30

    def changeImage(self, newImage):
        self.image = pygame.image.load(newImage)

