from random import randint

def pickComputerShips():
    compShipsx=[]
    compShipsy=[]
    i=0
    while i<=2:
        x=randint(0,9)
        y=randint(0,9)
        if len(compShipsx)>=1:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                x=randint(0,9)
                y=randint(0,9)
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
            if len(compShipsx)>=4:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
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
            if len(compShipsx)>=4:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
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
            if len(compShipsx)>=4:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
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
            if len(compShipsx)>=4:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
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
            if len(compShipsx)>=5:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                    x=randint(0,9)
                    y=randint(0,9)
            elif len(compShipsx)>=1:
                while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
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
        i+=1
    while i>=3 and i<=4:
        x=randint(0,9)
        y=randint(0,9)
        while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
            x=randint(0,9)
            y=randint(0,9)
        if x==9 and y==9 or x==8 and y==8 or x==8 and y==9 or x==9 and y==8:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] or (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)] and (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)]:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
                compShipsx.append(x*40)
                compShipsy.append((y-2)*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
                compShipsx.append((x-2)*40)
                compShipsy.append(y*40)
            else:
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
        elif x==0 and y==0 or x==1 and y==1 or x==1 and y==0 or x==0 and y==1:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] or (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)]:
                compShipsx.append(x*40)
                compShipsy.append((y+1)*40)
                compShipsx.append(x*40)
                compShipsy.append((y+2)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                compShipsx.append((x+1)*40)
                compShipsy.append(y*40)
                compShipsx.append((x+2)*40)
                compShipsy.append(y*40)
            else:
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
        elif x==0 and y==9 or x==1 and y==8 or x==0 and y==8 or x==1 and y==9:
#################            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] or (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)] and (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)]:
                compShipsx.append(x*40)
                compShipsy.append((y-1)*40)
                compShipsx.append(x*40)
                compShipsy.append((y-2)*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                compShipsx.append((x+1)*40)
                compShipsy.append(y*40)
                compShipsx.append((x+2)*40)
                compShipsy.append(y*40)
            else:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y-2)*40)
        elif x==9 and y==0 or x==8 and y==1 or x==9 and y==1 or x==8 and y==0:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] and (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)]:
                compShipsx.append(x*40)
                compShipsy.append((y+1)*40)
                compShipsx.append(x*40)
                compShipsy.append((y+2)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                compShipsx.append((x-1)*40)
                compShipsy.append(y*40)
                compShipsx.append((x-2)*40)
                compShipsy.append(y*40)
            else:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y+2)*40)
        elif x==9 or x==8:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                x=randint(0,9)
                y=randint(0,9)
            while (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)] and (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y+2)*40)
                elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y-2)*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y+2)*40)
                    else:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y-2)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                else:
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
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y+2)*40)
            else:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                elif choice==2:
                    compShipsx.append((x)*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append((x)*40)
                    compShipsy.append((y+2)*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y-2)*40)
        elif x==0 or x==1:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                x=randint(0,9)
                y=randint(0,9)
            while (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)] and (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y+2)*40)
                elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y-2)*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y+2)*40)
                    else:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y-2)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append(y*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append(y*40)
                        compShipsx.append((x+2)*40)
                        compShipsy.append(y*40)
                    else:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y-2)*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
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
            else:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append(y*40)
                elif choice==2:
                    compShipsx.append((x)*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append((x)*40)
                    compShipsy.append((y+2)*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y-2)*40)
        elif y==9 or y==8:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                x=randint(0,9)
                y=randint(0,9)
            while (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)] and (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)] and (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append((y)*40)
                elif (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y-2)*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
                        compShipsx.append((x+2)*40)
                        compShipsy.append((y)*40)
                    else:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y-2)*40)
            elif (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                else:
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
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
            else:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                elif choice==2:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append((y)*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y-2)*40)
        elif y==0 or y==1:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                x=randint(0,9)
                y=randint(0,9)
            while (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)] and (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)]:
                if (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append((y)*40)
                elif (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y+2)*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append((y)*40)
                        compShipsx.append((x+2)*40)
                        compShipsy.append((y)*40)
                    else:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y+2)*40)
            elif (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)]:
                if (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x-1)*40)
                        compShipsy.append(y*40)
                        compShipsx.append((x-2)*40)
                        compShipsy.append(y*40)
                    else:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y+2)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                choice=randint(1,2)
                if choice==1:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                else:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
            else:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append((x-1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append(y*40)
                elif choice==2:
                    compShipsx.append((x+1)*40)
                    compShipsy.append((y)*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append((y)*40)
                else:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y+2)*40)
        elif x==0 or x==1:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                x=randint(0,9)
                y=randint(0,9)
            while (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)] and (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y+2)*40)
                elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                    compShipsx.append(x*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append(x*40)
                    compShipsy.append((y-2)*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y+2)*40)
                    else:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y-2)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append(y*40)
                else:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append(y*40)
                        compShipsx.append((x+2)*40)
                        compShipsy.append(y*40)
                    else:
                        compShipsx.append(x*40)
                        compShipsy.append((y-1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y-2)*40)
        else:
            while (x*40) in compShipsx and (y*40)==compShipsy[compShipsx.index((x*40))]:
                x=randint(0,9)
                y=randint(0,9)
            while (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] and (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] and (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] and (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)] and (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)] and (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)] and (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                x=randint(0,9)
                y=randint(0,9)
            compShipsx.append((x*40))
            compShipsy.append((y*40))
            if (x+1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+1)*40)] or (x+2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x+2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)]:
                        compShipsx.append(x*40)
                        compShipsy.append((y+1)*40)
                        compShipsx.append(x*40)
                        compShipsy.append((y+2)*40)
                    elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                        compShipsx.append((x-1)*40)
                        compShipsy.append((y)*40)
                        compShipsx.append((x-2)*40)
                        compShipsy.append((y)*40)
                    else:
                        choice=randint(1,2)
                        if choice==1:
                            compShipsx.append(x*40)
                            compShipsy.append((y+1)*40)
                            compShipsx.append(x*40)
                            compShipsy.append((y+2)*40)
                        else:
                            compShipsx.append((x-1)*40)
                            compShipsy.append((y)*40)
                            compShipsx.append((x-2)*40)
                            compShipsy.append((y)*40)
            elif (y+1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+1)*40)] or (y+2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y+2)*40)]:
                if (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                    if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)]:
                        compShipsx.append((x+1)*40)
                        compShipsy.append(y*40)
                        compShipsx.append((x+2)*40)
                        compShipsy.append(y*40)
                    else:
                        choice=randint(1,2)
                        if choice==1:
                            compShipsx.append((x+1)*40)
                            compShipsy.append(y*40)
                            compShipsx.append((x+2)*40)
                            compShipsy.append(y*40)
                        else:
                            compShipsx.append((x-1)*40)
                            compShipsy.append((y)*40)
                            compShipsx.append((x-2)*40)
                            compShipsy.append((y)*40)
            elif (y-1)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-1)*40)] or (y-2)*40 in compShipsy and x*40==compShipsx[compShipsy.index((y-2)*40)]:
                if (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)]:
                    choice=randint(1,2)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append(y*40)
                        compShipsx.append((x+2)*40)
                        compShipsy.append(y*40)
                    else:
                        compShipsx.append((x)*40)
                        compShipsy.append((y+1)*40)
                        compShipsx.append((x)*40)
                        compShipsy.append((y+2)*40)
                else:
                    choice=randint(1,3)
                    if choice==1:
                        compShipsx.append((x+1)*40)
                        compShipsy.append(y*40)
                        compShipsx.append((x+2)*40)
                        compShipsy.append(y*40)
                    elif choice==2:
                        compShipsx.append((x-1)*40)
                        compShipsy.append(y*40)
                        compShipsx.append((x-2)*40)
                        compShipsy.append(y*40)
                    else:
                        compShipsx.append((x)*40)
                        compShipsy.append((y+1)*40)
                        compShipsx.append((x)*40)
                        compShipsy.append((y+2)*40)
            elif (x-1)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-1)*40)] or (x-2)*40 in compShipsx and y*40==compShipsy[compShipsx.index((x-2)*40)]:
                choice=randint(1,3)
                if choice==1:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append(y*40)
                elif choice==2:
                    compShipsx.append((x)*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append((x)*40)
                    compShipsy.append((y-2)*40)
                else:
                    compShipsx.append((x)*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append((x)*40)
                    compShipsy.append((y+2)*40)
            else:
                choice=randint(1,4)
                if choice==1:
                    compShipsx.append((x+1)*40)
                    compShipsy.append(y*40)
                    compShipsx.append((x+2)*40)
                    compShipsy.append(y*40)
                elif choice==2:
                    compShipsx.append((x)*40)
                    compShipsy.append((y-1)*40)
                    compShipsx.append((x)*40)
                    compShipsy.append((y-2)*40)
                elif choice==3:
                    compShipsx.append((x)*40)
                    compShipsy.append((y+1)*40)
                    compShipsx.append((x)*40)
                    compShipsy.append((y+2)*40)
                else:
                    compShipsx.append((x-1)*40)
                    compShipsy.append((y)*40)
                    compShipsx.append((x-2)*40)
                    compShipsy.append((y)*40)
        i+=1
    print(compShipsx)
    print(compShipsy)
pickComputerShips()
"""
    comp["compShipsx"]=compShipsx
    comp["compShipsy"]=compShipsy"""