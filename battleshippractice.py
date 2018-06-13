#Maia Reynolds
#5/22/18
#graphicsBattleship.py - Battleship with graphics

from ggame import *
from random import randint

def buildBoard():#makes 2 10x10 matrices and returns them
    rows=0
    columns=0
    while columns<400:
        while rows<400:
            Sprite(RectangleAsset(80,80,LineStyle(3,Color(0x104E8B,1)),Color(0x1874CD,1)),(rows,columns))
            rows+=80
        columns+=80
        rows=0
    columns=0
    while columns<400:
        while rows<400:
            Sprite(RectangleAsset(80,80,LineStyle(3,Color(0x104E8B,1)),Color(0x1874CD,1)),(600+rows,columns))
            rows+=80
        columns+=80
        rows=0
    return

#Has the computer pick 5 random spaces for their ships.
def pickComputerShips():
    i=0
    xl=[]
    yl=[]
    while i<=4:
        x=randint(0,4)
        y=randint(0,4)
        if len(xl)>0:
            if x in xl and y==yl[xl.index(x)]:#makes sure computer can't put ships in the same spot
                while x in xl and y==yl[xl.index(x)]:
                    x=randint(1,4)
                    y=randint(1,4)
        xl.append(x)
        yl.append(y)
        i+=1
    for item in xl:
        data["compShipsx"].append(item*80)#makes coordinates accessible to other functions
        data["compShipsy"].append(yl[xl.index(item)]*80)


#Computer picka a random spot to guess and process the guess if it is a valid move, detects if the computer won.
def computerTurn():
    x=randint(0,4)
    y=randint(0,4)
    if len(data["xmoves"])>=1:
        while x*80 in data["xmoves"] and y*80==data["ymoves"][data["xmoves"].index(x*80)]:
            x=randint(0,4)
            y=randint(0,4)
    data["ymoves"].append(y*80)#adds coordinates to list the computer doesn't repeat spot
    data["xmoves"].append(x*80)
    if (x*80) in data["yourShipsx"] and y*80==data["yourShipsy"][data["yourShipsx"].index((x*80))]:#if it hits
        Sprite(RectangleAsset(80,80,LineStyle(3,Color(0x104E8B,1)),Color(0xFF0000,1)),(x*80,y*80))
        data["compHit"]+=1
    else:#if it misses
        Sprite(RectangleAsset(80,80,LineStyle(3,Color(0x104E8B,1)),Color(0x000000,1)),(x*80,y*80))
    if data["compHit"]>=5:#if computer wins
        Sprite(RectangleAsset(2000,2000,LineStyle(1,Color(0x000000,1)),Color(0x000000,1)))
        Sprite(TextAsset("YouLose",fill=Color(0xFFFFFF,1),style="40pt Times bold"),(490,250))

#what row and column the user clicked (event.x and .y have the coordinates)
#if player hasnt placed ships, place ship, if has placed ship, process user's guess if valid and detect if player won
def mouseClick(event):
    data["click"]+=1
    if event.x<400 and event.y<400:#to place ships
        if data["click"]<=5:
            data["x1"]=(event.x-event.x%80)
            data["y1"]=(event.y-event.y%80)
            data["yourShipsx"].append(data["x1"])
            data["yourShipsy"].append(data["y1"])
            Sprite(RectangleAsset(80,80,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(data["x1"],data["y1"]))
    elif event.x>=600 and event.y<=400 and event.y>=0 and event.x<=1000:#on computer's side
        x=(event.x-((event.x-600)%80))
        y=(event.y-event.y%80)
        if x-600 in data["compShipsx"] and y==data["compShipsy"][data["compShipsx"].index(x-600)]:#if hit
            Sprite(RectangleAsset(80,80,LineStyle(3,Color(0xFF0000,1)),Color(0xFF3E96,1)),(x,y))
            data["Hits"]+=1
        else:#if miss
            Sprite(RectangleAsset(80,80,LineStyle(3,Color(0x000000,1)),Color(0x00F5FF,1)),(x,y))
        if data["Hits"]<5:#computer's turn
            computerTurn()
        else:#if you win
            Sprite(RectangleAsset(2000,2000,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)))
            Sprite(TextAsset("YouWin",fill=Color(0xFFFFFF,1),style="40pt Times bold"),(490,250))

if __name__ == '__main__':
    data={}
    data["click"]=0
    data["x1"]=0
    data["y1"]=0
    data["xmoves"]=[]
    data["ymoves"]=[]
    data["compHit"]=0
    data["Hits"]=0
    data["compShipsx"]=[]
    data["compShipsy"]=[]
    data["yourShipsx"]=[]
    data["yourShipsy"]=[]
    Sprite(TextAsset("Computer",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(725,400))
    Sprite(TextAsset("You",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(170,400))
    Sprite(TextAsset("Ships",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(455,0))
    Sprite(RectangleAsset(40,40,LineStyle(3,Color(0x104E8B,1)),Color(0xFF3E96,1)),(450,50))
    Sprite(TextAsset("x5",fill=Color(0xFF3030,1),style="30pt Georgia bold"),(495,50))
    buildBoard()
    pickComputerShips()

App().run()
App().listenMouseEvent("click",mouseClick)