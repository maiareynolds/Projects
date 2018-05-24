#Maia Reynolds
#5/22/18
#practicebattleship.py - practice Battleship

from ggame import *
from random import randint

def buildBoard():#makes 2 10x10 matrices and returns them
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
    return

#Deletes all graphics on the board and draws the player board and computer board in their current state
#allow for ships that are more than one space
def redrawAll():
    ...

#Has the computer pick 5 random spaces for their ships.
#The computer should not be able to put two ships on top of each other
def pickComputerShips():
    computerx=[]
    computery=[]
    computerx.append(randint(0,8))

#The function should have the computer pick a random spot to guess and process the guess if it is a valid move.
#This function should also detect if the computer won.
def computerTurn():
    ...

#what row and column the user clicked (event.x and .y have the coordinates)
#if player hasnt placed ships, place ship, if has placed ship, process user's guess if valid and detect if player won
def mouseClick(event):
    data["click"]+=1
    if event.x<400 and event.y<400:
        if data["click"]==1 or data["click"]==3 or data["click"]==5:
            data["x1"]=(event.x-event.x%40)
            data["y1"]=(event.y-event.y%40)
            data["yourships"].append(data["x1"])
            data["yourships"].append(data["y1"])
            data["option1"]=Sprite(RectangleAsset(120,40,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(data["x1"]-40,data["y1"]))
            data["option2"]=Sprite(RectangleAsset(40,120,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(data["x1"],data["y1"]-40))
            Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
        if data["click"]==2 or data["click"]==4 or data["click"]==6:
            data["option1"].destroy()
            data["option2"].destroy()
            data["x2"]=(event.x-event.x%40)
            data["y2"]=(event.y-event.y%40)
            data["yourships"].append(data["x2"])
            data["yourships"].append(data["y2"])
            if data["x2"]==data["x1"]-40:
                Sprite(RectangleAsset(80,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x2"],data["y2"]))
            elif data["x2"]==data["x1"]+40:
                Sprite(RectangleAsset(80,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
            elif data["y2"]==data["y1"]-40:
                Sprite(RectangleAsset(40,80,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x2"],data["y2"]))
            elif data["y2"]==data["y1"]+40:
                Sprite(RectangleAsset(40,80,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
            else:
                data["click"]-=1
        if data["click"]==7 or data["click"]==9:
            data["x1"]=(event.x-event.x%40)
            data["y1"]=(event.y-event.y%40)
            data["yourships"].append(data["x1"])
            data["yourships"].append(data["y1"])
            data["option1"]=Sprite(RectangleAsset(200,40,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(data["x1"]-80,data["y1"]))
            data["option2"]=Sprite(RectangleAsset(40,200,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(data["x1"],data["y1"]-80))
            Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
        if data["click"]==8 or data["click"]==10:
            data["option1"].destroy()
            data["option2"].destroy()
            data["x2"]=(event.x-event.x%40)
            data["y2"]=(event.y-event.y%40)
            data["yourships"].append(0)#fix
            data["yourships"].append(0)#fix
            data["yourships"].append(data["x2"])
            data["yourships"].append(data["y2"])
            if data["x2"]==data["x1"]-80:
                Sprite(RectangleAsset(120,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x2"],data["y2"]))
            elif data["x2"]==data["x1"]+80:
                Sprite(RectangleAsset(120,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
            elif data["y2"]==data["y1"]-80:
                Sprite(RectangleAsset(40,120,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x2"],data["y2"]))
            elif data["y2"]==data["y1"]+80:
                Sprite(RectangleAsset(40,120,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
            else:
                data["click"]-=1
    elif event.x>600 and event.y<400:
        x=(event.x-event.x%40)
        y=(event.y-event.y%40)
        Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(x,y))

#other color: 00F5FF

if __name__ == '__main__':
    data={}
    data["click"]=0
    data["x1"]=0
    data["y1"]=0
    data["x2"]=0
    data["y2"]=0
    data["option1"]=0
    data["option2"]=0
    data["yourships"]=[]
    print("To place your ships, click the box you want the ship to start in and the box you want it to end in")
    print("start with the two space ships and move to the three space ships")
    Sprite(TextAsset("Computer",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(725,400))
    Sprite(TextAsset("You",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(170,400))
    Sprite(TextAsset("Ships",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(455,0))
    Sprite(RectangleAsset(80,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(450,50))
    Sprite(TextAsset("x3",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(535,50))
    Sprite(RectangleAsset(120,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(410,100))
    Sprite(TextAsset("x2",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(535,100))
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
