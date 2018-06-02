from random import randint
"""
def pickComputerShips():
    compShips=[]
    i=0
    while i<=8:
        x=randint(0,9)
        y=randint(0,9)
        if len(compShips)>=2:
            while (x*40) in compShips and (y*40)==compShips[compShips.index((x*40))+1]:
                x=randint(0,9)
                y=randint(0,9)
            if len(compShips)>=5:
                while (x*40) in compShips and (y*40)==compShips[compShips.index((x*40))+1] and (x-1)*40 in compShips and y*40==compShips[compShips.index((x-1)*40)+1] and (y-1)*40 in compShips and x*40==compShips[compShips.index((y-1)*40)-1] and (x+1)*40 in compShips and y*40==compShips[compShips.index((x+1)*40)+1] and (y+1)*40 in compShips and x*40==compShips[compShips.index((y+1)*40)-1]:
                    x=randint(0,9)
                    y=randint(0,9)
        compShips.append((x*40))
        compShips.append((y*40))
        i+=1
    print(compShips)
"""

def pickComputerShips():
    compShipsx=[]
    compShipsy=[]
    i=0
    while i<=1:
        x=randint(0,9)
        y=randint(0,9)
        if len(compShipsx)>=1:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))+1]:
                x=randint(0,9)
                y=randint(0,9)
            if len(compShipsx)>=5:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
        compShipsx.append((x*40))
        compShipsy.append((y*40))

###################


        if x==9 and y==9:
            if len(compShipsx)>=3:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                    x=randint(0,9)
                    y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
            else:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
        elif x==0 and y==0:
            if len(compShipsx)>=3:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                    x=randint(0,9)
                    y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                compShipsx.append(x*40)
                compShipsy.append((y+1)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                compShipsx.append((x+1)*40)
                compShipsy.append(y*40)
            else:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
        elif x==0 and y==9:
            if len(compShipsx)>=3:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                    x=randint(0,9)
                    y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                compShipsx.append((x+1)*40)
                compShipsy.append(y*40)
            else:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
        elif x==9 and y==0:
            if len(compShipsx)>=3:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                    x=randint(0,9)
                    y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                compShipsx.append(x*40)
                compShipsy.append((y+1)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
            else:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
        elif x==9:
            if len(compShipsx)>=3:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                    x=randint(0,9)
                    y=randint(0,9)
            
            
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                    else:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                if (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                    else:
                        compShipsx.append((x-1)*40)
                        compShipsy.append((y)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                else:
                    compShipsx.append((x-1)*40)
                    compShipsy.append((y)*40)
            else:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                elif choice==2:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                else:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
        elif y==9:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                elif (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                    compShipsx.append((x)*40)
                    compShipsy.append((y-1)*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                    else:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
                    else:
                        compShipsx.append((x-1)*40)
                        compShipsy.append((y)*40)
            elif (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                else:
                    compShipsx.append((x-1)*40)
                    compShipsy.append((y)*40)
            else:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                elif choice==2:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                else:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
        elif y==0:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                if (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                elif (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                    compShipsx.append((x)*40)
                    compShipsy.append((y+1)*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                    else:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
                    else:
                        compShipsx.append((x-1)*40)
                        compShipsy.append((y)*40)
            elif (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                else:
                    compShipsx.append((x-1)*40)
                    compShipsy.append((y)*40)
            else:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                elif choice==2:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                else:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
        elif x==0:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                    compShipsx.append((x)*40)
                    compShipsy.append((y+1)*40)
                elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    compShipsx.append((x)*40)
                    compShipsy.append((y-1)*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                    else:
                        compShipsx.append((x)*40)
                        compShipsy.append((y+1)*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                if (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
                    else:
                        compShipsx.append((x)*40)
                        compShipsy.append((y+1)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                else:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
            else:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                elif choice==2:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                else:
                    compShipsx.append((x)*40)
                    compShipsy.append((y+1)*40)
        else:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                    if (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                        compShipsx.append((x-1)*40)
                        compShipsy.append((y)*40)
                    elif (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                        compShipsx.append((x)*40)
                        compShipsy.append((y+1)*40)
                    else:
                        choice=randint(1,2)
                        if choice==1:
                            compShipsx.append(x*40)
                            compShipsy.append((y+1)*40)
                        else:
                            compShipsx.append((x-1)*40)
                            compShipsy.append((y)*40)
                elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                        compShipsx.append((x)*40)
                        compShipsy.append((y-1)*40)
                    else:
                        choice=randint(1,2)
                        if choice==1:
                            compShipsx.append(x*40)
                            compShipsy.append((y-1)*40)
                        else:
                            compShipsx.append((x-1)*40)
                            compShipsy.append((y)*40)
                elif (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                    else:
                        compShipsx.append((x)*40)
                        compShipsy.append((y+1)*40)
                else:
                    choice=randint(1,3)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                    elif choice==2:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                    else:
                        compShipsx.append((x-1)*40)
                        compShipsy.append(y*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                    if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
                    else:
                        choice=randint(1,2)
                        if choice==1:
                            compShipsx.append((x+1)*40)
                            compShipsy.append((y)*40)
                        else:
                            compShipsx.append((x-1)*40)
                            compShipsy.append((y)*40)
                elif (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
                    else:
                        compShipsx.append((x)*40)
                        compShipsy.append((y-1)*40)
                else:
                    choice=randint(1,3)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                    elif choice==2:
                        compShipsx.append((x+1)*40)
                        compShipsy.append(y*40)
                    else:
                        compShipsx.append((x-1)*40)
                        compShipsy.append(y*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)]:
                if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
                    else:
                        compShipsx.append((x)*40)
                        compShipsy.append((y+1)*40)
                else:
                    choice=randint(1,3)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                    elif choice==2:
                        compShipsx.append((x+1)*40)
                        compShipsy.append(y*40)
                    else:
                        compShipsx.append((x-1)*40)
                        compShipsy.append(y*40)
            elif (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)]:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                elif choice==2:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append((x)*40)
                    compShipsy.append((y-1)*40)
            else:
                choice=randint(1,4)
                if choice==1:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                elif choice==2:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                elif choice==3:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)




########################

        i+=1
    while i>1 and i<=4:
        x=randint(0,9)
        y=randint(0,9)
        compShipsx.append(x*40)
        compShipsy.append(y*40)
        if x==9 and y==9:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
                compShipsx.append((x-2)*40)
                compShipsy.append(y*40)
            else:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
                compShipsx.append(x*40)
                compShipsy.append((y-2)*40)
        elif x==0 and y==0:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append((x+1)*40)
                compShipsy.append(y*40)
                compShipsx.append((x+2)*40)
                compShipsy.append(y*40)
            else:
                compShipsx.append(x*40)
                compShipsy.append((y+1)*40)
                compShipsx.append(x*40)
                compShipsy.append((y+2)*40)
        elif x==9:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
                compShipsx.append(x*40)
                compShipsy.append((y+1)*40)
            else:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
                compShipsx.append((x-2)*40)
                compShipsy.append(y*40)
        elif y==9:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
                compShipsx.append((x+1)*40)
                compShipsy.append(y*40)
            else:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
                compShipsx.append(x*40)
                compShipsy.append((y-2)*40)
        else:
            choice=randint(1,2)
            if choice==1:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
                compShipsx.append(x*40)
                compShipsy.append((y+1)*40)
            else:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
                compShipsx.append((x+1)*40)
                compShipsy.append(y*40)
        i+=1
        print(compShipsx)
        print(compShipsy)
pickComputerShips()
"""
    comp["compShipsx"]=compShipsx
    comp["compShipsy"]=compShipsy"""