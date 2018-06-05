from math import *

list1=["e**(x/2)","e**(x)","(log(x)/log(e))**x","x**x"]
num=[]

x=100
functions=[e**(x/2),e**(x),(log(x)/log(e))**x,x**x]
l=len(functions)
newlist=[]

"""
while l!=len(newlist):
    for item in functions:
        if item==max(functions):
            newlist.append(item)
            num.append(functions.index(item))
            functions.remove(item)
"""

while l!=len(newlist):
    for item in functions:
        if item==max(functions):
            num.append(functions.index(item))
            functions.remove(item)
    for item in num:
        newlist.append(list1[item])

print(newlist)