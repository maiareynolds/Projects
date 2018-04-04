#Maia Reynolds
#4/4/18
#graphicsHangman.py - hangman with graphics

from ggame import *
from random import randint

def pickWord: #picks a "random" word from a list of words
    i=randint(1,5)
    if i==1:
        word=""
    elif i==2:
        word=""
    elif i==3:
        word=""
    elif i==4:
        word=""
    else:
        word=""

def wordComplete: #returns True if all letters in word have been guessed, false otherwise
    ...

def printHangman(incorrect): #prints out new body part with each wrong guess
    if incorrect==1:
        Sprite(...

def keyPress(event): #puts letter in word if correct and  puts letter in list of guessed letters
    

if __name__=="__main__":
    ...



"""
-------------------------------------------------------
Useful detail - event.key contains the key that was pressed to trigger the key press function. You will need to listen for 26 different keys (use a loop to shorten this code!)

-------------------------------------------------------
Ideas for extensions:
1) Make your graphics really cool (animation?)
2) Come up with a scoring system
3) Make different levels (easy, medium, hard)
4) Research which words are the hardest to guess"""
