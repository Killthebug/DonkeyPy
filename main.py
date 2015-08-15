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

class App():
    def __init__(self):
#Important to begin and initialize everything
        pygame.init()

#Determine the dimension
        self.display_Width = 1200
        self.display_Height = 600
        self.image_Width = 30
        self.image_Height = 30

#Setup the Display
        self.DISPLAYSURF = pygame.display.set_mode((self.display_Width , self.display_Height))
        pygame.display.set_caption('DonkeyPy')

#Define the colors
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.blue = (0,0,128)
        self.red = (255,0,0)

#Set up the self.clock for the game and decide Frame Rate
        self.clock = pygame.time.Clock()
        self.FPS = 30

#Introduce self.fonts
        self.font = pygame.font.SysFont(None, 25) # self.font Size 25

#Alias Directions
        self.UP = 'up'
        self.DOWN = 'down'
        self.LEFT = 'left'
        self.RIGHT = 'right'

        self.big_list = pygame.sprite.Group()

#Introduce our players
        self.donkey = Donkey()
        self.big_list.add(self.donkey)

#Introduce the Queen
        self.queen = Queen(150,68)
        self.queen_list = pygame.sprite.Group()
        self.queen_list.add(self.queen)

#Introduce the Boards
        self.board = Board(0,0)
        self.block_list = pygame.sprite.Group()

#Introduce the Ladders
        self.ladder_list = pygame.sprite.Group()
        self.ladder_1 = Ladder()
        self.ladder_list.add(self.ladder_1)
        self.ladder_2 = Ladder()
        self.ladder_list.add(self.ladder_2)
        self.ladder_3 = Ladder()
        self.ladder_list.add(self.ladder_3)
        self.ladder_4 = Ladder()
        self.ladder_list.add(self.ladder_4)
        self.ladder_5 = Ladder()
        self.ladder_list.add(self.ladder_5)

#Introduce the Bananas
        self.banana_list = pygame.sprite.Group()

#Bring Home the Fire !
        self.fire_list = pygame.sprite.Group()

#Introduce the Villian
        self.man = Human()
        self.great_list = pygame.sprite.Group()


    def makeFire(self):
        self.fireball = Fire(0,0)
        self.fireball.x = self.man.x
        self.fireball.y = 104
        self.fireball.rect.x = self.fireball.x
        self.fireball.rect.y = self.fireball.y
        self.fire_list.add(self.fireball)


    def makeBananas(self,quantity,check):
        if check == 0 :
            for bananas in self.banana_list:
                self.banana_list.remove(bananas)
            for i in range(quantity/4):
                self.banana = Banana(0,0)
                self.banana.x = random.randrange(0,self.display_Width-40,30)
                self.banana.y = 538
                self.banana.rect.x = self.banana.x
                self.banana.rect.y = self.banana.y
                self.banana_list.add(self.banana)
                self.big_list.add(self.banana)
            for i in range(quantity/4):
                self.banana = Banana(0,0)
                self.banana.x = random.randrange(100,1000,30)
                self.banana.y = 438
                self.banana.rect.x = self.banana.x
                self.banana.rect.y = self.banana.y
                self.banana_list.add(self.banana)
                self.big_list.add(self.banana)
            for i in range(quantity/4):
                self.banana = Banana(0,0)
                self.banana.x = random.randrange(300,self.display_Width-40,30)
                self.banana.y = 288
                self.banana.rect.x = self.banana.x
                self.banana.rect.y = self.banana.y
                self.banana_list.add(self.banana)
                self.big_list.add(self.banana)
            for i in range(quantity/4):
                self.banana = Banana(0,0)
                self.banana.x = random.randrange(0,900,30)
                self.banana.y = 188
                self.banana.rect.x = self.banana.x
                self.banana.rect.y = self.banana.y
                self.banana_list.add(self.banana)
                self.big_list.add(self.banana)

    def changePosition(self, ladder, x, y):
        """ Function modifies the postion of the ladder """
        ladder.x = x
        ladder.y = y


    def makeLadders(self):
        self.changePosition(self.ladder_1,200,150)
        self.renderImage(self.ladder_1.body, self.ladder_1.x, self.ladder_1.y)
        self.changePosition(self.ladder_2,400,250)
        self.renderImage(self.ladder_2.body, self.ladder_2.x, self.ladder_2.y)
        self.changePosition(self.ladder_3,800,350)
        self.renderImage(self.ladder_3.body, self.ladder_3.x, self.ladder_3.y)
        self.changePosition(self.ladder_4,800,395)
        self.renderImage(self.ladder_4.body, self.ladder_4.x, self.ladder_4.y)
        self.changePosition(self.ladder_5,546,500)
        self.renderImage(self.ladder_5.body, self.ladder_5.x, self.ladder_5.y)

    def generateBoard(self,check):
        if check == 0:
            for i in range(0,45):
                self.new_block = Board(i*30,570)
                self.block_list.add(self.new_block)
                self.DISPLAYSURF.blit(self.board.image,(i*30,570))
            for i in range(0,30):
                self.new_block = Board(100+i*30,470)
                self.block_list.add(self.new_block)
                self.DISPLAYSURF.blit(self.board.image,(100+i*30,470))
            for i in range(0,30):
                self.new_block = Board(300+i*30,320)
                self.block_list.add(self.new_block)
                self.DISPLAYSURF.blit(self.board.image,(300+i*30,320))
            for i in range(0,30):
                self.new_block = Board(i*30,220)
                self.block_list.add(self.new_block)
                self.DISPLAYSURF.blit(self.board.image,(i*30,220))
            for i in range(0,15):
                self.new_block = Board(150+i*30,120)
                self.block_list.add(self.new_block)
                self.DISPLAYSURF.blit(self.board.image,(150+i*30,120))
        else:
            for baba in self.block_list:
                self.DISPLAYSURF.blit(baba.image,(baba.x,baba.y))

    def gravity(self):
        self.gravity_list = pygame.sprite.Group()
        self.gravity_list = pygame.sprite.spritecollide(self.donkey, self.block_list, False)
        if len(self.gravity_list) == 0 and self.donkey.canClimbUp == False:
            self.donkey.y = self.donkey.y + 1.5

    def printMessage(self,msg, color, x, y):
        self.show_text = self.font.render(msg, True, color)
        self.DISPLAYSURF.blit(self.show_text,[x,y])

    def boundaryCheck(self):
        if self.donkey.x > self.display_Width - self.image_Width or self.donkey.x < 0 or self.donkey.canMoveSide == False:
            self.donkey.x_Stop()
        if self.donkey.y > 538:
            self.donkey.y_Stop()

    def canClimb(self):
        self.m = self.donkey.x
        self.y = self.donkey.y
        if self.m > self.ladder_1.x-15 and self.m <self.ladder_1.x+15:
            if self.y <= self.ladder_1.y+42 and self.y >= self.ladder_1.y-62:
                self.donkey.canClimbUp = True
            else:
                self.donkey.canClimbUp = False
        elif self.m > self.ladder_2.x-15 and self.m <self.ladder_2.x+15:
            if self.y <= self.ladder_2.y+42 and self.y >= self.ladder_2.y-62:
                self.donkey.canClimbUp = True
            else:
                self.donkey.canClimbUp = False
        elif self.m > self.ladder_3.x-15 and self.m <self.ladder_3.x+15:
            if self.y <= self.ladder_3.y+50 and self.y >= self.ladder_3.y-62:
                self.donkey.canClimbUp = True
            elif self.y <= self.ladder_4.y+44 and self.y >= self.ladder_4.y-62:
                self.donkey.canClimbUp = True
            else:
                self.donkey.canClimbUp = False
        elif self.m > self.ladder_5.x-15 and self.m <self.ladder_5.x+15:
            if self.y <= self.ladder_5.y+70 and self.y >= self.ladder_5.y-62:
                self.donkey.canClimbUp = True
            else:
                self.donkey.canClimbUp = False

    def canHorizontal(self):
        self.m = self.donkey.x
        self.y = self.donkey.y
        if self.m > self.ladder_1.x-30 and self.m <self.ladder_1.x+30:
            if self.y <= self.ladder_1.y+37 and self.y >= self.ladder_1.y-57:
                self.donkey.canMoveSide = False
            else:
                self.donkey.canMoveSide = True
        elif self.m > self.ladder_2.x-30 and self.m <self.ladder_2.x+30:
            if self.y <= self.ladder_2.y+37 and self.y >= self.ladder_2.y-57:
                self.donkey.canMoveSide = False
            else:
                self.donkey.canMoveSide = True
        elif self.m > self.ladder_3.x-30 and self.m <self.ladder_3.x+30:
            if self.y <= self.ladder_3.y+50 and self.y >= self.ladder_3.y-57:
                self.donkey.canMoveSide = False
            elif self.y <= self.ladder_4.y and self.y >= self.ladder_4.y-62:
                self.donkey.canMoveSide = False
            else:
                self.donkey.canMoveSide = True
        elif self.m > self.ladder_5.x-30 and self.m <self.ladder_5.x+30:
            if self.y <= self.ladder_5.y+37 and self.y >= self.ladder_5.y-57:
                self.donkey.canMoveSide = False
            else:
                self.donkey.canMoveSide = True
        else:
            self.donkey.canMoveSide = True
        
    def canFallDown(self):
        for fires in self.fire_list:
            self.m = fires.x
            self.y = fires.y
            if self.m > self.ladder_1.x-15 and self.m <self.ladder_1.x+15:
                if self.y <= self.ladder_1.y+50 and self.y >= self.ladder_1.y-62:
                    fires.canFallDown = True
                else:
                    fires.canFallDown = False
            elif self.m > self.ladder_2.x-15 and self.m <self.ladder_2.x+15:
                if self.y <= self.ladder_2.y+50 and self.y >= self.ladder_2.y-62:
                    fires.canFallDown = True
                else:
                    fires.canFallDown = False
            elif self.m > self.ladder_3.x-15 and self.m <self.ladder_3.x+15:
                if self.y <= self.ladder_3.y+50 and self.y >= self.ladder_3.y-62:
                    fires.canFallDown = True
                elif self.y <= self.ladder_4.y+50 and self.y >= self.ladder_4.y-62:
                    fires.canFallDown = True
                else:
                    fires.canFallDown = False
            elif self.m > self.ladder_5.x-15 and self.m <self.ladder_5.x+15:
                if self.y <= self.ladder_5.y+50 and self.y >= self.ladder_5.y-62:
                    fires.canFallDown = True
                else:
                    fires.canFallDown = False
            else:
                fires.canFallDown = False

    def getPosition(self,body):
        self.pos = [body.x , body.y]
        return self.pos

    def checkWall_Up(self):
        self.canClimb()
        if self.donkey.canClimbUp == False:
            self.donkey.y_Stop()

    def checkWall_Down(self):
        self.canClimb()
        if self.donkey.canClimbUp == False:
            self.donkey.y_Stop()

    def Jump(self):
        if self.donkey.canJump == True:
            for i in range(210):
                self.donkey.Jump()
                self.renderImage(self.donkey.body, self.donkey.x, self.donkey.y)
        self.platform_hit_list = pygame.sprite.spritecollide(self.donkey, self.block_list, False)
        if len(self.platform_hit_list) == 0:
            self.donkey.canJump = False
        else:
            self.donkey.canJump = True

    def handleFire(self):
        self.canFallDown()
        for fires in self.fire_list:
            if fires.canFallDown == True :
                fires.moveDown()
            self.DISPLAYSURF.blit(fires.image,(fires.x,fires.y))

    def collectCoin(self):
        self.block_hit_list = pygame.sprite.spritecollide(self.donkey,self.banana_list,True)
        if len(self.block_hit_list)>0:
            self.donkey.score += len(self.block_hit_list)*5

    def checkCollision(self):
        for fires in self.fire_list:
            self.handleFire()
            self.fire_hit_list = pygame.sprite.spritecollide(fires, self.block_list, False)
            fires.find_Level()
            fires.moveWeird()
            self.player_fire_hit_list = pygame.sprite.spritecollide(self.donkey, self.fire_list, True)
            if len(self.player_fire_hit_list) > 0:
                self.donkey.lives -= 1
                self.donkey.resetPos()

    def checkGameStatus(self):
        self.win_list = pygame.sprite.spritecollide(self.donkey, self.queen_list, False)
        if len(self.win_list) > 0:
            self.donkey.score += 50
            self.donkey.win = True
            return True
        else:
            return False

    def renderImage(self,body,x,y):
        self.DISPLAYSURF.blit(body,(x,y))

    def main(self):
        self.gameOver = False
        self.gameOverDone = False
        self.check = 0
        self.counter = 0
        while not self.gameOverDone:
            if self.donkey.lives <= 0:
                self.donkey.Penalize()
                self.donkey.win = False
                self.gameOver = True
                self.gameOverDone = False
            
            while self.gameOver == True:
                self.DISPLAYSURF.fill(self.black)
                self.message = "Final Score : "+str(self.donkey.score)
                self.message2 = "Game Over "
                self.message3 = "Thanks For Playing!"
                self.message4 = "Press 'q' to : Quit"
                self.message5 = "Press 'r' to : Reset"
                self.printMessage(self.message, self.white, 490, 350)
                self.printMessage(self.message4, self.white, 485, 370)
                self.printMessage(self.message5, self.white, 482, 390)
                self.printMessage(self.message2, self.red, 510, 250)
                self.printMessage(self.message3, self.red, 470, 280)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.gameOverDone = False
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.donkey.newGame()
                            for fires in self.fire_list:
                                self.fire_list.remove(fires)
                            self.gameOver = False
                            self.check = 0
                        if event.key == pygame.K_q:
                            self.gameOverDone = False
                            pygame.quit()
                            quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOverDone = False
                    pygame.quit()
                    quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.donkey.moveLeft()
                    self.canHorizontal()

                elif event.key == pygame.K_d:
                    self.donkey.moveRight()
                    self.canHorizontal()

                elif event.key == pygame.K_w:
                    self.donkey.moveUp()
                    self.checkWall_Up()

                elif event.key == pygame.K_s:
                    self.donkey.moveDown()
                    self.checkWall_Down()

                elif event.key == pygame.K_SPACE:
                    self.Jump()

            if event.type == pygame.KEYUP:
                self.donkey.reset()

            #Increment Counter
            self.counter += 1

            #The very first and bottom most layer
            self.DISPLAYSURF.fill(self.black)
            
            #Once the background has been generated we make the board
            self.generateBoard(self.check)
            
            #MoveHuman
            self.man.Update(220,600)

            #MakeBananas
            self.makeBananas(20,self.check)
           
            #MakeFire
            if self.counter % 120 == 0 :
                self.makeFire()
            
            self.check = 1
           
            #Implement Gravity
            self.gravity()

            #Make the ladders
            self.makeLadders()

            #Function Call the check if over flow occurs
            self.boundaryCheck()

            self.donkey.canClimbUp = False
            self.donkey.update()  
            
            #self.fire_list.draw(self.DISPLAYSURF)
            self.checkCollision()
            
            self.banana_list.draw(self.DISPLAYSURF)
            self.collectCoin()

            #Change the Display location of the self.donkey
            self.renderImage(self.donkey.body, self.donkey.x, self.donkey.y)
            self.renderImage(self.man.player, self.man.x, self.man.y)
            self.renderImage(self.queen.image, self.queen.rect.x, self.queen.rect.y)
            
            #Constantly Check if the Game is over
            self.gameOver = self.checkGameStatus()
            
            #Showing the message
            self.message = "Score : "+str(self.donkey.score)
            self.printMessage(self.message, self.white, 1100, 10)
            self.message = " Lives : "+str(self.donkey.lives)
            self.printMessage(self.message, self.white, 1100, 40)

            #Update the screen to show the latest changes
            pygame.display.update()
            self.clock.tick(60)

#Initiate main running loop
if __name__ == '__main__': 
    theGame = App()
    theGame.main()
