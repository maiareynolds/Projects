from math import *

x=10000
functions=[e**(x/2),e**(x),(log(x)/log(e))**x,x**x]
l=len(functions)
newlist=[]

while l!=len(newlist):
    for item in functions:
        if item==max(functions):
            newlist.append(item)
            functions.remove(item)