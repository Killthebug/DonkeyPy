#The lady, the donkey is after

import pygame
import time
import os
import sys
from pygame import *

class Queen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('queen_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

