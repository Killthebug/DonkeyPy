#!/usr/bin/python

#############################################################################
# File name : donkeyKong.py
# Purpose : A game for SSAD : Assignment 1
# Start date : 11/08/2015
# Author : Jaipal Singh Goud
############################################################################

import re
import os
import sys
import pygame
import time
import math
import getopt
import random
import Person
import Board
import Donkey
from socket import *
from pygame.locals import *
from Person import *
from Donkey import *
from Board import *

#Important to begin and initialize everything
pygame.init()

#Determine the dimension
display_Width = 1200
display_Height = 450
image_Width = 30
image_Height = 30

#Setup the Display
DISPLAYSURF = pygame.display.set_mode((display_Width , display_Height))
pygame.display.set_caption('Donkeypy')

#Define the colors
white = (255,255,255)
black = (0,0,0)
blue = (0,0,128)
red = (255,0,0)
green = (0,128,0)

#Set up the clock for the game and decide Frame Rate
clock = pygame.time.Clock()
FPS = 30

#Alias Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

#Introduce our players
donkey = Donkey()

#Introduce the Boards
board = Board()

def generateBoard():
    for i in range(0,45):
        DISPLAYSURF.blit(board.image,(i*30,420))
    for i in range(0,30):
        DISPLAYSURF.blit(board.image,(300+i*30,300))
    for i in range(0,30):
        DISPLAYSURF.blit(board.image,(i*30,180))
    for i in range(0,15):
        DISPLAYSURF.blit(board.image,(150+i*30,80))


def boundaryCheck():
    if donkey.x > display_Width - image_Width or donkey.x < 0:
        donkey.stop()

def renderImage(body,x,y):
    DISPLAYSURF.blit(body,(x,y))

def main():
    gameOver = False

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                donkey.moveLeft()

            elif event.key == pygame.K_RIGHT:
                donkey.moveRight()

            elif event.key == pygame.K_UP:
                donkey.moveUp()

            elif event.key == pygame.K_DOWN:
                donkey.moveDown()

        if event.type == pygame.KEYUP:
            donkey.reset()

        #The very first and bottom most layer
        DISPLAYSURF.fill(blue)
        
        #Once the background has been generated we make the board
        generateBoard()
        
        #Function Call the check if over flow occurs
        boundaryCheck()

        #Change the Display location of the Donkey
        renderImage(donkey.body, donkey.x, donkey.y)

        #Update the screen to show the latest changes
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__': 
    main()
    pygame.quit()
    quit()
