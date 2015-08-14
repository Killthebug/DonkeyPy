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
import Human
import Board
import Donkey
import Ladder
from socket import *
from pygame.locals import *
from Person import *
from Donkey import *
from Board import *
from Human import *
from Ladder import *

#Important to begin and initialize everything
pygame.init()

#Determine the dimension
display_Width = 1200
display_Height = 600
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

#Introduce the Ladders
ladder_1 = Ladder()
ladder_2 = Ladder()
ladder_3 = Ladder()
ladder_4 = Ladder()
ladder_5 = Ladder()

#Introduce the Villian
man = Human()

def changePosition(ladder, x, y):
    """ Function modifies the postion of the ladder """
    ladder.x = x
    ladder.y = y

def canClimb():
    m = donkey.x
    n = donkey.y
    if m > ladder_1.x-10 and m <ladder_1.x+10:
        donkey.canClimbUp = True
    elif m > ladder_2.x-10 and m <ladder_2.x+10:
        donkey.canClimbUp = True
    elif m > ladder_3.x-10 and m <ladder_3.x+10:
        donkey.canClimbUp = True
    elif m > ladder_4.x-10 and m <ladder_4.x+10:
        donkey.canClimbUp = True
    elif m > ladder_5.x-10 and m <ladder_5.x+10:
        donkey.canClimbUp = True
    else:
        donkey.canClimbUp = False

def makeLadders():
    changePosition(ladder_1,200,150)
    renderImage(ladder_1.body, ladder_1.x, ladder_1.y)
    changePosition(ladder_2,400,250)
    renderImage(ladder_2.body, ladder_2.x, ladder_2.y)
    changePosition(ladder_3,800,350)
    renderImage(ladder_3.body, ladder_3.x, ladder_3.y)
    changePosition(ladder_4,800,395)
    renderImage(ladder_4.body, ladder_4.x, ladder_4.y)
    changePosition(ladder_5,546,500)
    renderImage(ladder_5.body, ladder_5.x, ladder_5.y)

def generateBoard():
    for i in range(0,45):
        DISPLAYSURF.blit(board.image,(i*30,570))
    for i in range(0,30):
        DISPLAYSURF.blit(board.image,(100+i*30,470))
    for i in range(0,30):
        DISPLAYSURF.blit(board.image,(300+i*30,320))
    for i in range(0,30):
        DISPLAYSURF.blit(board.image,(i*30,220))
    for i in range(0,15):
        DISPLAYSURF.blit(board.image,(150+i*30,120))

def boundaryCheck():
    if donkey.x > display_Width - image_Width or donkey.x < 0:
        donkey.x_Stop()
    if donkey.y > 538:
        donkey.y_Stop()

def canGoUp():
    y = donkey.y
    canClimb()
    if donkey.canClimbUp == True:
        if y <= ladder_1.y+70 and y >= ladder_1.y-60:
            donkey.canClimbUp = True
        elif y <= ladder_2.y+70 and y >= ladder_2.y-60:
            donkey.canClimbUp = True
        elif y <= ladder_3.y+70 and y >= ladder_3.y-60:
            donkey.canClimbUp = True
        elif y <= ladder_4.y+70 and y >= ladder_4.y-60:
            donkey.canClimbUp = True
        elif y <= ladder_5.y+70 and y >= ladder_5.y-60:
            donkey.canClimbUp = True
        else :
            donkey.canClimbUp = False
    if donkey.canClimbUp == False:
        donkey.y_Stop()

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
                canGoUp()

            elif event.key == pygame.K_DOWN:
                donkey.moveDown()
        
        if event.type == pygame.KEYUP:
            donkey.reset()
            donkey.canClimbUp = False

        #The very first and bottom most layer
        DISPLAYSURF.fill(blue)
        
        #Once the background has been generated we make the board
        generateBoard()
        
        #Make the ladders
        makeLadders()

        #Function Call the check if over flow occurs
        boundaryCheck()

        #Change the Display location of the Donkey
        renderImage(donkey.body, donkey.x, donkey.y)
        renderImage(man.player, man.x, man.y)

        #Update the screen to show the latest changes
        pygame.display.update()
        clock.tick(40)


if __name__ == '__main__': 
    main()
    pygame.quit()
    quit()
