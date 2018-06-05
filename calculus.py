from math import *
#f=[e**(x/2),e**(x),(log(x)/log(e))**x,x**x]



list1=["x**2","e**(x/2)","e**(x*(2/3))","x**3"]
num=[]

x=100000000000000000000000
functions=[x**2,e**(x/2),e**(x*(2/3)),x**3]
functions1=[x**2,e**(x/2),e**(x*(2/3)),x**3]
l=len(functions)
newlist=[]
newlist1=[]

"""
while l!=len(newlist):
    for item in functions:
        if item==max(functions):
            newlist.append(item)
            num.append(functions.index(item))
            functions.remove(item)
"""

while l>len(newlist):
    for item in functions:
        if item==max(functions):
            num.append(functions1.index(item))
            newlist.append(item)
            functions.remove(item)
for item in num:
    newlist1.append(list1[item])



print(newlist1)