#!/usr/bin/python

#############################################################################
# File name : donkeyKong.py
# Purpose : A game for SSAD : Assignment 1
# Game Difficult : High
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
import Queen
import Donkey
import Ladder
import Fire
from socket import *
from pygame.locals import *
from Person import *
from Donkey import *
from Board import *
from Human import *
from Ladder import *
from Banana import *
from time import *
from Fire import *
from Queen import *

#Important to begin and initialize everything
pygame.init()

#Determine the dimension
display_Width = 1200
display_Height = 600
image_Width = 30
image_Height = 30

#Setup the Display
DISPLAYSURF = pygame.display.set_mode((display_Width , display_Height))
pygame.display.set_caption('DonkeyPy')

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

#Introduce the Queen
queen = Queen(150,68)
queen_list = pygame.sprite.Group()
queen_list.add(queen)

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

#Bring Home the Fire !
fire_list = pygame.sprite.Group()

def makeFire():
    fireball = Fire(0,0)
    fireball.x = man.x
    fireball.y = 104
    fireball.rect.x = fireball.x
    fireball.rect.y = fireball.y
    fire_list.add(fireball)


#Introduce the Bananas
banana_list = pygame.sprite.Group()

def makeBananas(quantity,check):
    if check == 0 :
        for bananas in banana_list:
            banana_list.remove(bananas)
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
        donkey.y = donkey.y + 1.5

def printMessage(msg, color, x, y):
    show_text = font.render(msg, True, color)
    DISPLAYSURF.blit(show_text,[x,y])

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
    
def canFallDown():
    for fires in fire_list:
        m = fires.x
        y = fires.y
        if m > ladder_1.x-15 and m <ladder_1.x+15:
            if y <= ladder_1.y+50 and y >= ladder_1.y-62:
                fires.canFallDown = True
            else:
                fires.canFallDown = False
        elif m > ladder_2.x-15 and m <ladder_2.x+15:
            if y <= ladder_2.y+50 and y >= ladder_2.y-62:
                fires.canFallDown = True
            else:
                fires.canFallDown = False
        elif m > ladder_3.x-15 and m <ladder_3.x+15:
            if y <= ladder_3.y+50 and y >= ladder_3.y-62:
                fires.canFallDown = True
            elif y <= ladder_4.y+50 and y >= ladder_4.y-62:
                fires.canFallDown = True
            else:
                fires.canFallDown = False
        elif m > ladder_5.x-15 and m <ladder_5.x+15:
            if y <= ladder_5.y+50 and y >= ladder_5.y-62:
                fires.canFallDown = True
            else:
                fires.canFallDown = False
        else:
            fires.canFallDown = False

def getPosition(body):
    pos = [body.x , body.y]
    return pos

def checkWall_Up():
    canClimb()
    if donkey.canClimbUp == False:
        donkey.y_Stop()

def checkWall_Down():
    canClimb()
    if donkey.canClimbUp == False:
        donkey.y_Stop()

def Jump():
    if donkey.canJump == True:
        for i in range(210):
            donkey.Jump()
            renderImage(donkey.body, donkey.x, donkey.y)
    platform_hit_list = pygame.sprite.spritecollide(donkey, block_list, False)
    if len(platform_hit_list) == 0:
        donkey.canJump = False
    else:
        donkey.canJump = True

def handleFire():
    canFallDown()
    for fires in fire_list:
        if fires.canFallDown == True :
            fires.moveDown()
        DISPLAYSURF.blit(fires.image,(fires.x,fires.y))

def collectCoin():
    block_hit_list = pygame.sprite.spritecollide(donkey,banana_list,True)
    if len(block_hit_list)>0:
        donkey.score += len(block_hit_list)*5

def checkCollision():
    for fires in fire_list:
        handleFire()
        fire_hit_list = pygame.sprite.spritecollide(fires, block_list, False)
        fires.find_Level()
        fires.moveWeird()
        player_fire_hit_list = pygame.sprite.spritecollide(donkey, fire_list, True)
        if len(player_fire_hit_list) > 0:
            donkey.lives -= 1
            donkey.resetPos()

def checkGameStatus():
    win_list = pygame.sprite.spritecollide(donkey, queen_list, False)
    if len(win_list) > 0:
        donkey.score += 50
        donkey.win = True
        return True
    else:
        return False

def renderImage(body,x,y):
    DISPLAYSURF.blit(body,(x,y))

def main():
    gameOver = False
    gameOverDone = False
    check = 0
    counter = 0
    while not gameOverDone:
        if donkey.lives <= 0:
            donkey.Penalize()
            donkey.win = False
            gameOver = True
            gameOverDone = False
        
        while gameOver == True:
            DISPLAYSURF.fill(black)
            message = "Final Score : "+str(donkey.score)
            message2 = "Game Over "
            message3 = "Thanks For Playing!"
            message4 = "Press 'q' to : Quit"
            message5 = "Press 'r' to : Reset"
            printMessage(message, white, 490, 350)
            printMessage(message4, white, 485, 370)
            printMessage(message5, white, 482, 390)
            printMessage(message2, red, 510, 250)
            printMessage(message3, red, 470, 280)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOverDone = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        donkey.newGame()
                        for fires in fire_list:
                            fire_list.remove(fires)
                        gameOver = False
                        check = 0
                    if event.key == pygame.K_q:
                        gameOverDone = False
                        pygame.quit()
                        quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOverDone = False
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                donkey.moveLeft()
                canHorizontal()

            elif event.key == pygame.K_d:
                donkey.moveRight()
                canHorizontal()

            elif event.key == pygame.K_w:
                donkey.moveUp()
                checkWall_Up()

            elif event.key == pygame.K_s:
                donkey.moveDown()
                checkWall_Down()

            elif event.key == pygame.K_SPACE:
                Jump()

        if event.type == pygame.KEYUP:
            donkey.reset()

        #Increment Counter
        counter += 1

        #The very first and bottom most layer
        DISPLAYSURF.fill(black)
        
        #Once the background has been generated we make the board
        generateBoard(check)
        
        #MoveHuman
        man.Update(220,600)

        #MakeBananas
        makeBananas(20,check)
       
        #MakeFire
        if counter % 120 == 0 :
            makeFire()
        
        check = 1
       
        #Implement Gravity
        gravity()

        #Make the ladders
        makeLadders()

        #Function Call the check if over flow occurs
        boundaryCheck()

        donkey.canClimbUp = False
        donkey.update()  
        
        #fire_list.draw(DISPLAYSURF)
        checkCollision()
        
        banana_list.draw(DISPLAYSURF)
        collectCoin()

        #Change the Display location of the Donkey
        renderImage(donkey.body, donkey.x, donkey.y)
        renderImage(man.player, man.x, man.y)
        renderImage(queen.image, queen.rect.x, queen.rect.y)
        
        #Constantly Check if the Game is over
        gameOver = checkGameStatus()
        
        #Showing the message
        message = "Score : "+str(donkey.score)
        printMessage(message, white, 1100, 10)
        message = " Lives : "+str(donkey.lives)
        printMessage(message, white, 1100, 40)

        #Update the screen to show the latest changes
        pygame.display.update()
        clock.tick(60)

#Initiate main running loop
if __name__ == '__main__': 
    main()
    pygame.quit()
    quit()
