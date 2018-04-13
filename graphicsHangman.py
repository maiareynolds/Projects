#Maia Reynolds
#4/4/18
#graphicsHangman.py - hangman with graphics

from ggame import *
from random import randint
"""
def pickWord(): #picks a "random" word from a list of words
    i=randint(1,5)
    if i==1:
        word="Awkward"
    elif i==2:
        word="Croquet"
    elif i==3:
        word="Fjord"
    elif i==4:
        word="Kiosk"
    else:
        word="Quip"

def wordComplete(): #returns True if all letters in word have been guessed, false otherwise
    Sprite(RectangleAsset(1200,800,LineStyle(3,Color(0xBBFFFF,1)),Color(0xBBFFFF,1)))
    Sprite(RectangleAsset(1200,400,LineStyle(3,Color(0x00FF7F,1)),Color(0x00FF7F,1)),(0,300))
    Sprite(TextAsset("True, the word is",fill=Color(0xFF1493,1),style="40pt Times bold"),(150,150)))#work on
    Sprite(TextAsset(word,fill=Color(0xFF1493,1),style="40pt Times bold",(250,200)))

    if str(data["letter"]) not in str(data["word"]):
"""
def printHangman(incorrect): #prints out new body part with each wrong guess
    while incorrect<=6:
        if incorrect==1:
            Sprite(CircleAsset(15,LineStyle(1,Color(0xFF1493,1)),Color(0xFF1493,1)),(292.5,95))#head
        elif incorrect==2:
            Sprite(LineAsset(0,70,LineStyle(4,Color(0xFF1493,1))),(303,120))#body
        elif incorrect==3:
            Sprite(LineAsset(30,30,LineStyle(4,Color(0xFF1493,1))),(274,125))#arm1
        elif incorrect==4:
            Sprite(LineAsset(-30,30,LineStyle(4,Color(0xFF1493,1))),(303,125))#arm2
        elif incorrect==5:
            Sprite(LineAsset(-30,30,LineStyle(4,Color(0xFF1493,1))),(274,190))#leg1
        else:
            Sprite(LineAsset(30,30,LineStyle(4,Color(0xFF1493,1))),(303,190))#leg2
    Sprite(RectangleAsset(1100,600,LineStyle(4,Color(0x000000,1)),Color(0x000000,1)))
    Sprite(TextAsset("False",fill=Color(0xFF0000,1),style="60pt Times bold"),(420,200))
    Sprite(TextAsset("Game"+"Over",fill=Color(0xFF0000,1),style="60pt Times bold"),(325,260))

def keyPress(event): #puts letter in word if correct and  puts letter in list of guessed letters
    letter=event.key
    data["letter"]=letter
    print(data["letter"])#take out
    x1=0
    if letter not in word:
        data["incorrect"]+=1
        printHangman(data["incorrect"])
    else:
        for ch in word:
            if letter==ch:
                Sprite(TextAsset(letter,fill=Color(0x000000,1),style="15pt Times"),(135+x1,325))
            x1+=30
        x1+=30
        data["correct"]+=1
        if data["correct"]==:
            wordComplete()
    Sprite(TextAsset(letter,fill=Color(0x000000,1),style="15pt Times"),(x1,0))#FIX


if __name__=="__main__":
    data={}
    data["letter"]=0
    data["incorrect"]=0
    data["correct"]=0
    data["letter"]=0
    word="watermelon"
    data["word"]=word
    #Background Graphics
    Sprite(RectangleAsset(1200,800,LineStyle(3,Color(0x9FB6CD,1)),Color(0x9FB6CD,1)))#sky
    Sprite(RectangleAsset(1200,400,LineStyle(3,Color(0x8B4726,1)),Color(0x8B4726,1)),(0,300))#ground
    Sprite(RectangleAsset(1200,40,LineStyle(3,Color(0x5CACEE,1)),Color(0x5CACEE,1)))#letter box
    #Structure Graphic:
    Sprite(LineAsset(0,250,LineStyle(6,Color(0x000000,1))),(200,50))#large down
    Sprite(LineAsset(100,0,LineStyle(6,Color(0x000000,1))),(200,50))#small across
    Sprite(LineAsset(0,40,LineStyle(6,Color(0x000000,1))),(300,50))#small down
    Sprite(LineAsset(150,0,LineStyle(6,Color(0x000000,1))),(125,300))#large across
    Sprite(TextAsset("Hangman",fill=Color(0x00CED1,1),style="15pt Times"),(930,500))#logo
    #Letter Line Graphics
    x=0
    for ch in word:
        Sprite(LineAsset(20,0,LineStyle(3,Color(0x000000,1))),(125+x,350))
        x+=30

"""
#Man Graphics
Sprite(CircleAsset(15,LineStyle(1,Color(0xFF1493,1)),Color(0xFF1493,1)),(292.5,95))#head
Sprite(LineAsset(0,70,LineStyle(4,Color(0xFF1493,1))),(303,120))#body
Sprite(LineAsset(30,30,LineStyle(4,Color(0xFF1493,1))),(274,125))#arm1
Sprite(LineAsset(-30,30,LineStyle(4,Color(0xFF1493,1))),(303,125))#arm2
Sprite(LineAsset(-30,30,LineStyle(4,Color(0xFF1493,1))),(274,190))#leg1
Sprite(LineAsset(30,30,LineStyle(4,Color(0xFF1493,1))),(303,190))#leg2
"""
App().listenKeyEvent("keydown","a",keyPress)
App().listenKeyEvent("keydown","b",keyPress)
App().listenKeyEvent("keydown","c",keyPress)
App().listenKeyEvent("keydown","d",keyPress)
App().listenKeyEvent("keydown","e",keyPress)
App().listenKeyEvent("keydown","f",keyPress)
App().listenKeyEvent("keydown","g",keyPress)
App().listenKeyEvent("keydown","h",keyPress)
App().listenKeyEvent("keydown","i",keyPress)
App().listenKeyEvent("keydown","j",keyPress)
App().listenKeyEvent("keydown","k",keyPress)
App().listenKeyEvent("keydown","l",keyPress)
App().listenKeyEvent("keydown","m",keyPress)
App().listenKeyEvent("keydown","n",keyPress)
App().listenKeyEvent("keydown","o",keyPress)
App().listenKeyEvent("keydown","p",keyPress)
App().listenKeyEvent("keydown","q",keyPress)
App().listenKeyEvent("keydown","r",keyPress)
App().listenKeyEvent("keydown","s",keyPress)
App().listenKeyEvent("keydown","t",keyPress)
App().listenKeyEvent("keydown","u",keyPress)
App().listenKeyEvent("keydown","v",keyPress)
App().listenKeyEvent("keydown","w",keyPress)
App().listenKeyEvent("keydown","x",keyPress)
App().listenKeyEvent("keydown","y",keyPress)
App().listenKeyEvent("keydown","z",keyPress)

App().run()

"""
#consider adding difficulty levels

-------------------------------------------------------
Useful detail - event.key contains the key that was pressed to trigger the key press function. You will need to listen for 26 different keys (use a loop to shorten this code!)

-------------------------------------------------------
Ideas for extensions:
1) Make your graphics really cool (animation?)
2) Come up with a scoring system
3) Make different levels (easy, medium, hard)
4) Research which words are the hardest to guess"""
