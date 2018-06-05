from math import *
#f=[e**(x/2),e**(x),(log(x)/log(e))**x,x**x]

list1=["e**(x/2)","e**(x)","(log(x)/log(e))**x","x**x"]
num=[]

x=100000
functions=[e**(x/2),e**(x),(log(x)/log(e))**x,x**x]
functions1=[e**(x/2),e**(x),(log(x)/log(e))**x,x**x]
l=len(functions)
newlist=[]

while len(functions)>0:
    i=0
    for item in functions:
        if item>=i:
            i=item
    newlist.append(list1[functions1.index(i)])
    functions.remove(i)

print(newlist)


"""
while 0<len(functions):
    for item in functions:
        if item==max(functions):
            num.append(functions1.index(item))
            functions.remove(item)
for item in num:
    newlist.append(list1[item])

print(newlist)
"""