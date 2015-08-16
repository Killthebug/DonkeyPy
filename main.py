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
import Banana
import Donkey
import Ladder
from socket import *
from pygame.locals import *
from Person import *
from Donkey import *
from Board import *
from Human import *
from Ladder import *
from Banana import *
from time import *

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

#Introduce fonts
font = pygame.font.SysFont(None, 25) # Font Size 25

#Alias Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

big_list = pygame.sprite.Group()

#Introduce our players
donkey = Donkey()
big_list.add(donkey)

#Introduce the Boards
board = Board(0,0)
block_list = pygame.sprite.Group()

#Introduce the Ladders
ladder_list = pygame.sprite.Group()
ladder_1 = Ladder()
ladder_list.add(ladder_1)
ladder_2 = Ladder()
ladder_list.add(ladder_2)
ladder_3 = Ladder()
ladder_list.add(ladder_3)
ladder_4 = Ladder()
ladder_list.add(ladder_4)
ladder_5 = Ladder()
ladder_list.add(ladder_5)

#Introduce the Bananas
banana_list = pygame.sprite.Group()

def makeBananas(quantity,check):
    if check == 0 :
        for i in range(quantity/4):
            banana = Banana(0,0)
            banana.x = random.randrange(0,display_Width-40,30)
            banana.y = 538
            banana.rect.x = banana.x
            banana.rect.y = banana.y
            banana_list.add(banana)
            big_list.add(banana)
        for i in range(quantity/4):
            banana = Banana(0,0)
            banana.x = random.randrange(100,1000,30)
            banana.y = 438
            banana.rect.x = banana.x
            banana.rect.y = banana.y
            banana_list.add(banana)
            big_list.add(banana)
        for i in range(quantity/4):
            banana = Banana(0,0)
            banana.x = random.randrange(300,display_Width-40,30)
            banana.y = 288
            banana.rect.x = banana.x
            banana.rect.y = banana.y
            banana_list.add(banana)
            big_list.add(banana)
        for i in range(quantity/4):
            banana = Banana(0,0)
            banana.x = random.randrange(0,900,30)
            banana.y = 188
            banana.rect.x = banana.x
            banana.rect.y = banana.y
            banana_list.add(banana)
            big_list.add(banana)

#Introduce the Villian
man = Human()
great_list = pygame.sprite.Group()

def changePosition(ladder, x, y):
    """ Function modifies the postion of the ladder """
    ladder.x = x
    ladder.y = y


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

def generateBoard(check):
    if check == 0:
        for i in range(0,45):
            new_block = Board(i*30,570)
            block_list.add(new_block)
            DISPLAYSURF.blit(board.image,(i*30,570))
        for i in range(0,30):
            new_block = Board(100+i*30,470)
            block_list.add(new_block)
            DISPLAYSURF.blit(board.image,(100+i*30,470))
        for i in range(0,30):
            new_block = Board(300+i*30,320)
            block_list.add(new_block)
            DISPLAYSURF.blit(board.image,(300+i*30,320))
        for i in range(0,30):
            new_block = Board(i*30,220)
            block_list.add(new_block)
            DISPLAYSURF.blit(board.image,(i*30,220))
        for i in range(0,15):
            new_block = Board(150+i*30,120)
            block_list.add(new_block)
            DISPLAYSURF.blit(board.image,(150+i*30,120))
    else:
        for baba in block_list:
            DISPLAYSURF.blit(baba.image,(baba.x,baba.y))

def gravity():
    gravity_list = pygame.sprite.Group()
    gravity_list = pygame.sprite.spritecollide(donkey, block_list, False)
    if len(gravity_list) == 0 and donkey.canClimbUp == False:
        donkey.y = donkey.y + 3
    print gravity_list

def printMessage(msg, color):
    show_text = font.render(msg, True, color)
    DISPLAYSURF.blit(show_text,[1100,10])

def boundaryCheck():
    if donkey.x > display_Width - image_Width or donkey.x < 0 or donkey.canMoveSide == False:
        donkey.x_Stop()
    if donkey.y > 538:
        donkey.y_Stop()

def canClimb():
    m = donkey.x
    y = donkey.y
    if m > ladder_1.x-15 and m <ladder_1.x+15:
        if y <= ladder_1.y+42 and y >= ladder_1.y-62:
            donkey.canClimbUp = True
        else:
            donkey.canClimbUp = False
    elif m > ladder_2.x-15 and m <ladder_2.x+15:
        if y <= ladder_2.y+42 and y >= ladder_2.y-62:
            donkey.canClimbUp = True
        else:
            donkey.canClimbUp = False
    elif m > ladder_3.x-15 and m <ladder_3.x+15:
        if y <= ladder_3.y+50 and y >= ladder_3.y-62:
            donkey.canClimbUp = True
        elif y <= ladder_4.y+44 and y >= ladder_4.y-62:
            donkey.canClimbUp = True
        else:
            donkey.canClimbUp = False
    elif m > ladder_5.x-15 and m <ladder_5.x+15:
        if y <= ladder_5.y+70 and y >= ladder_5.y-62:
            donkey.canClimbUp = True
        else:
            donkey.canClimbUp = False

def canHorizontal():
    m = donkey.x
    y = donkey.y
    if m > ladder_1.x-30 and m <ladder_1.x+30:
        if y <= ladder_1.y+37 and y >= ladder_1.y-57:
            donkey.canMoveSide = False
        else:
            donkey.canMoveSide = True
    elif m > ladder_2.x-30 and m <ladder_2.x+30:
        if y <= ladder_2.y+37 and y >= ladder_2.y-57:
            donkey.canMoveSide = False
        else:
            donkey.canMoveSide = True
    elif m > ladder_3.x-30 and m <ladder_3.x+30:
        if y <= ladder_3.y+50 and y >= ladder_3.y-57:
            donkey.canMoveSide = False
        elif y <= ladder_4.y and y >= ladder_4.y-62:
            donkey.canMoveSide = False
        else:
            donkey.canMoveSide = True
    elif m > ladder_5.x-30 and m <ladder_5.x+30:
        if y <= ladder_5.y+37 and y >= ladder_5.y-57:
            donkey.canMoveSide = False
        else:
            donkey.canMoveSide = True
    else:
        donkey.canMoveSide = True

def canGoUp():
    canClimb()
    if donkey.canClimbUp == False:
        donkey.y_Stop()

def canGoDown():
    canClimb()
    if donkey.canClimbUp == False:
        donkey.y_Stop()

def Jump():
    if donkey.canJump == True:
        donkey.Jump()
    platform_hit_list = pygame.sprite.spritecollide(donkey, block_list, False)
    if len(platform_hit_list) == 0:
        donkey.canJump = False
    else:
        donkey.canJump = True

def renderImage(body,x,y):
    DISPLAYSURF.blit(body,(x,y))

def main():
    gameOver = False
    check = 0
    score = 0
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                donkey.moveLeft()
                canHorizontal()

            elif event.key == pygame.K_RIGHT:
                donkey.moveRight()
                canHorizontal()

            elif event.key == pygame.K_UP:
                donkey.moveUp()
                canGoUp()

            elif event.key == pygame.K_DOWN:
                donkey.moveDown()
                canGoDown()

            elif event.key == pygame.K_SPACE:
                Jump()

        if event.type == pygame.KEYUP:
            donkey.reset()

        #The very first and bottom most layer
        DISPLAYSURF.fill(blue)
        
        #Once the background has been generated we make the board
        generateBoard(check)
        
        #MoveHuman
        man.update(150,600)

        #MakeBananas
        makeBananas(16,check)
        check = 1
        
        gravity()

        #Make the ladders
        makeLadders()

        #Function Call the check if over flow occurs
        boundaryCheck()

        donkey.canClimbUp = False
        donkey.update()  
        banana_list.draw(DISPLAYSURF)
        block_hit_list = pygame.sprite.spritecollide(donkey,banana_list,True)
        
        if len(block_hit_list)>0:
            score += len(block_hit_list)
            print score

        #Change the Display location of the Donkey
        renderImage(donkey.body, donkey.x, donkey.y)
        renderImage(man.player, man.x, man.y)
        
        #Showing the message
        message = "Score : "+str(score)
        printMessage(message, white)
        print block_list        

        #Update the screen to show the latest changes
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__': 
    main()
    pygame.quit()
    quit()
