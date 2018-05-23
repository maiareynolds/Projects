#Maia Reynolds
#5/22/18
#practicebattleship.py - practice Battleship

from ggame import *
from random import randint

#makes 2 10x10 matrices and returns them
def buildBoard():
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
    Sprite(TextAsset("Computer",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(725,400))
    Sprite(TextAsset("You",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(170,400))
    Sprite(TextAsset("Ships",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(455,0))
    Sprite(RectangleAsset(80,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(450,50))
    Sprite(TextAsset("x3",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(535,50))
    Sprite(RectangleAsset(120,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(410,100))
    Sprite(TextAsset("x2",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(535,100))
    return

#Deletes all graphics on the board and draws the player board and computer board in their current state
#allow for ships that are more than one space
def redrawAll():
    ...

#Has the computer pick 5 random spaces for their ships.
#The computer should not be able to put two ships on top of each other
def pickComputerShips():
    ...

#The function should have the computer pick a random spot to guess and process the guess if it is a valid move.
#This function should also detect if the computer won.
def computerTurn():
    ...

#what row and column the user clicked (event.x and .y have the coordinates)
#if player hasnt placed ships, place ship, if has placed ship, process user's guess if valid and detect if player won
squares=0
def mouseClick(event):
    squares+=1
    for squares<=11
        if event.x<400 and event.y<400:
            x=(event.x-event.x%40)
            y=(event.y-event.y%40)
            Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(x,y))

if __name__ == '__main__':
    buildBoard()

App().run()
App().listenMouseEvent("click",mouseClick)
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
