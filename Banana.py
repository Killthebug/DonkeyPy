import pygame
import sys
import re
import os
from pygame import *

class Banana(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('banana.png')
        self.x = x;
        self.y = y;
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
