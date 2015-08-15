import pygame
import os
import sys
from pygame import *

class Person():
    """ Parent class giving basic Life Attributes """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 5
        self.x_Change = 0
        self.y_Change = 0
        self.body = None
        self.canMoveSide = True

    def moveLeft(self):
        self.x_Change = -5
        self.x = self.x + self.x_Change

    def moveRight(self):
        self.x_Chnage = 5
        self.x = self.x + self.x_Change

    def moveUp(self):
        self.y_Change = 5
        self.y = self.y - self.y_Change

    def moveDown(self):
        self.y_Change = -5
        self.y = self.y - self.y_Change

    def reset(self):
        self.y_Change = 0
        self.x_Change = 0

