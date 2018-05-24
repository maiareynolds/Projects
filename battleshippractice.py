#Maia Reynolds
#5/22/18
#practicebattleship.py - practice Battleship

#Questions:
#How to make universal lists?



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
    compShipsx=[]
    compShipsy=[]
    i=0
    for i<=2:
        x=randint(0,9)
        y=randint(0,9)
        compShipsx.append(x*40)
        compShipsy.append(y*40)
        if x==9 and y==9:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
            else:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
        elif x==0 and y==0:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append((x+1)*40)
                compShipsy.append(y*40)
            else:
                compShipsx.append(x*40)
                compShipsy.append((y+1)*40)
        elif x==9:
            choice=randint(1,3)
            if choice==1:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
            elif choice==2:
                compShipsx.append(x*40)
                compShipsy.append((y+1)*40)
            else:
                compShipsx.append((x-1)*40)
                compShipsy.append(y)
        elif y==9:
            choice=randint(1,3)
            if choice==1:
                compShipsx.append(x-1)
                compShipsy.append(y)
            elif choice==2:
                compShipsx.append(x+1)
                compShipsy.append(y)
            else:
                compShipsx.append(x)
                compShipsy.append(y-1)
        else:
            choice=randint(1,4)
            if choice==1:
                compShipsx.append(x)
                compShipsy.append(y-1)
            elif choice==2:
                compShipsx.append(x)
                compShipsy.append(y+1)
            elif choice==3:
                compShipsx.append(x+1)
                compShipsy.append(y)
            else:
                compShipsx.append(x-1)
                compShipsy.append(y)
        i+=1
    for i>2 and i<=4:
        x=randint(0,9)
        y=randint(0,9)
        compShipsx.append(x*40)
        compShipsy.append(y*40)
        if x==9 and y==9:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
                compShipsx.append(x-2)
                compShipsy.append(y)
            else:
                compShipsx.append(x)
                compShipsy.append(y-1)
                compShipsx.append(x)
                compShipsy.append(y-2)
        elif x==0 and y==0:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append(x+1)
                compShipsy.append(y)
                compShipsx.append(x+2)
                compShipsy.append(y)
            else:
                compShipsx.append(x)
                compShipsy.append(y+1)
                compShipsx.append(x)
                compShipsy.append(y+2)
        elif x==9:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append(x)
                compShipsy.append(y-1)
                compShipsx.append(x)
                compShipsy.append(y+1)
            else:
                compShipsx.append(x-1)
                compShipsy.append(y)
                compShipsx.append(x-2)
                compShipsy.append(y)
        elif y==9:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append(x-1)
                compShipsy.append(y)
                compShipsx.append(x+1)
                compShipsy.append(y)
            else:
                compShipsx.append(x)
                compShipsy.append(y-1)
                compShipsx.append(x)
                compShipsy.append(y-2)
        else:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append(x)
                compShipsy.append(y-1)
                compShipsx.append(x)
                compShipsy.append(y+1)
            else:
                compShipsx.append(x-1)
                compShipsy.append(y)
                compShipsx.append(x+1)
                compShipsy.append(y)
        i+=1
    for x*40 in yourShips:
        if y*40==yourShips[yourShips.index(x*40)+1]:
            Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF0000,1)),(x*40,y*40))
            data["compHits"]+=1
            point=True
    if point==False:
        Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(x*40,y*40))
    if data["compHits"]==12:
        Sprite(RectangleAsset(1000,1000,LineStyle(1,Color(0x000000,1)),Color(0x000000,1)))
        Sprite(TextAsset("You Lose",fill=Color(0xFFFFFF,1),style="40pt Times bold"),(490,250)
    comp["xmoves"]=xmoves
    comp["ymoves"]=ymoves

        choice=randint(
        compShipsx.append(x)
        compShipsy.append(y)
        compShipsx.append(x
        i+=1
    comp["compShipsx"]=compShips

#The function should have the computer pick a random spot to guess and process the guess if it is a valid move.
#This function should also detect if the computer won.
def computerTurn():
    ymoves=[]
    xmoves=[]
    x=randint(0,9)
    y=randint(0,9)
    for x*40 in xmoves:
        if y*40==ymoves[xmoves.index(x*40)]:
            computerTurn()
    ymoves.append(y*40)
    xmoves.append(x*40)
    point=False
    for x*40 in yourShips:
        if y*40==yourShips[yourShips.index(x*40)+1]:
            Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF0000,1)),(x*40,y*40))
            data["compHits"]+=1
            point=True
    if point==False:
        Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(x*40,y*40))
    if data["compHits"]==12:
        Sprite(RectangleAsset(1000,1000,LineStyle(1,Color(0x000000,1)),Color(0x000000,1)))
        Sprite(TextAsset("You Lose",fill=Color(0xFFFFFF,1),style="40pt Times bold"),(490,250)
    comp["xmoves"]=xmoves
    comp["ymoves"]=ymoves
"""
#what row and column the user clicked (event.x and .y have the coordinates)
#if player hasnt placed ships, place ship, if has placed ship, process user's guess if valid and detect if player won
def mouseClick(event):
    data["click"]+=1
    yourShips=[]
    if event.x<400 and event.y<400:
        if data["click"]==1 or data["click"]==3 or data["click"]==5:
            data["x1"]=(event.x-event.x%40)
            data["y1"]=(event.y-event.y%40)
            data["yourShips"].append(data["x1"])
            data["yourShips"].append(data["y1"])
            data["option1"]=Sprite(RectangleAsset(120,40,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(data["x1"]-40,data["y1"]))
            data["option2"]=Sprite(RectangleAsset(40,120,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(data["x1"],data["y1"]-40))
            Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
        elif data["click"]==2 or data["click"]==4 or data["click"]==6:
            data["option1"].destroy()
            data["option2"].destroy()
            data["x2"]=(event.x-event.x%40)
            data["y2"]=(event.y-event.y%40)
            data["yourShips"].append(data["x2"])
            data["yourShips"].append(data["y2"])
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
        elif data["click"]==7 or data["click"]==9:
            data["x1"]=(event.x-event.x%40)
            data["y1"]=(event.y-event.y%40)
            data["yourShips"].append(data["x1"])
            data["yourShips"].append(data["y1"])
            data["option1"]=Sprite(RectangleAsset(200,40,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(data["x1"]-80,data["y1"]))
            data["option2"]=Sprite(RectangleAsset(40,200,LineStyle(3,Color(0x104E8B,1)),Color(0xEE82EE,1)),(data["x1"],data["y1"]-80))
            Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
        elif data["click"]==8 or data["click"]==10:
            data["option1"].destroy()
            data["option2"].destroy()
            data["x2"]=(event.x-event.x%40)
            data["y2"]=(event.y-event.y%40)
            if data["x2"]==data["x1"]-80:
                data["yourShips"].append((data["x1"]-40))
                data["yourShips"].append(data["y1"])
                data["yourShips"].append(data["x2"])
                data["yourShips"].append(data["y2"])
                Sprite(RectangleAsset(120,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x2"],data["y2"]))
            elif data["x2"]==data["x1"]+80:
                data["yourShips"].append((data["x1"]+40))
                data["yourShips"].append(data["y1"])
                data["yourShips"].append(data["x2"])
                data["yourShips"].append(data["y2"])
                Sprite(RectangleAsset(120,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
            elif data["y2"]==data["y1"]-80:
                data["yourShips"].append((data["x1"]))
                data["yourShips"].append((data["y1"]-40))
                data["yourShips"].append(data["x2"])
                data["yourShips"].append(data["y2"])
                Sprite(RectangleAsset(40,120,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x2"],data["y2"]))
            elif data["y2"]==data["y1"]+80:
                data["yourShips"].append((data["x1"]))
                data["yourShips"].append((data["y1"]+40))
                data["yourShips"].append(data["x2"])
                data["yourShips"].append(data["y2"])
                Sprite(RectangleAsset(40,120,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
            else:
                data["click"]-=1
    elif event.x>600 and event.y<400:
        if data["click"]<=11:
            x=(event.x-event.x%40)
            y=(event.y-event.y%40)
            i=0
            for i<=24:
                if list(data["compShips"])[i]==x and list(data["compShips"])[i+1]==y:
                    Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(x,y))
                    data["Hits"]+=1
                else:
                    Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0x00F5FF,1)),(x,y))
                i+=2
            computerTurn()
    if data["Hits"]==12:
        print("you win")#fix
"""
#other color: 00F5FF

if __name__ == '__main__':
    data={}
    data["click"]=0
    data["x1"]=0
    data["y1"]=0
    data["x2"]=0
    data["y2"]=0
    data["x3"]=0
    data["y3"]=0
    data["option1"]=0
    data["option2"]=0
    data["yourShips"]=0#what to do
    data["compShips"]=0#what to do
    data["compHit"]=0
    data["Hits"]=0
    comp={"xmoves","ymoves","compShipsx","compShipsy"}
    you={}
    Sprite(TextAsset("Computer",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(725,400))
    Sprite(TextAsset("You",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(170,400))
    Sprite(TextAsset("Ships",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(455,0))
    Sprite(RectangleAsset(80,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(450,50))
    Sprite(TextAsset("x3",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(535,50))
    Sprite(RectangleAsset(120,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(410,100))
    Sprite(TextAsset("x2",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(535,100))
    buildBoard()
    pickComputerShips()

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