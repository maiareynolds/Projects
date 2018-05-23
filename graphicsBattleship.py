#Maia Reynolds
#5/22/18
#graphicsBattleship.py - Battleship with graphics

from ggame import *

def buildBoard(): #5x5 matrix (or whatever size) and returns it
    Sprite(RectangleAsset(400,400,LineStyle(1,Color(0x1874CD,1)),Color(0x1874CD,1)))#need?
    rows=0
    columns=0
    while columns<400:
        while rows<400:
            Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0x1874CD,1)),(rows,columns))
            rows+=40
        columns+=40
        rows=0
    columns=0
    while columns<400:
        while rows<400:
            Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0x1874CD,1)),(600+rows,columns))
            rows+=40
        columns+=40
        rows=0

#Deletes all graphics on the board and draws the player board and computer board in their current state
#allow for ships that are more than one space
def redrawAll():
    ...

#Has the computer pick three random spaces for their ships.
#The computer should not be able to put two ships on top of each other
def pickComputerShips():
    ...

#The function should have the computer pick a random spot to guess and process the guess if it is a valid move.
#This function should also detect if the computer won.
def computerTurn():
    ...

#what row and column the used clicked (event.x and .y have the coordinates)
#if player hasnt placed ships, place ship, if user has placed ship, process user's guess if valid and detect if player won
def mouseClick(event):
    ...

if __name__ == '__main__':
    buildBoard()

#second color:104E8B

App().run()
#look at matrix demo
#To delete all graphics, you can use a for loop.
#for item in App().spritelist[:]:
#    item.destroy()
#I used some constants like EMPTY = 0, MISS = 1, HIT = 2,make it easier to keep track of the numbers in the matrices.

#Ideas for extensions:
#1) Make a two player version
#2) Allow for ships that are more than one space
#3) Allow the user to chose the board size and/or the number of ships.
#4) Make a cool animation when a ship is sunk.