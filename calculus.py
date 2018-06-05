from math import *
#f=[e**(x/2),e**(x),(log(x)/log(e))**x,x**x]

list1=["e**(x/2)","e**(x)","(log(x)/log(e))**x","x**x"]
num=[]

x=100000
functions=[e**(x/2),e**(x),(log(x)/log(e))**x,x**x]
functions1=[e**(x/2),e**(x),(log(x)/log(e))**x,x**x]
l=len(functions)
newlist=[]
newlist1=[]

while 0<len(newlist):
    for item in functions:
        if item==max(functions):
            num.append(functions1.index(item))
            functions.remove(item)
for item in num:
    newlist1.append(list1[item])

print(newlist1)