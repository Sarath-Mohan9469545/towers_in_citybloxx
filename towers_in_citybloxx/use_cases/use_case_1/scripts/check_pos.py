def checkpos(l,us,ds,ls,rs):
    for i in range(len(l)):
        for j in range(len(l)):
            ijlist=[0,len(l)-1]

            if i in ijlist and j in ijlist:
                if l[i][j]=="y":
                    l[i][j]="g"
                else:
                    if i==0 and j==0:
                        if l[i][j]=="g": 
                            if "b" in [l[i][j+1],l[i+1][j]] and "r" in [l[i][j+1],l[i+1][j]]:
                                continue
                            else:
                                l[i][j]="r"
                                continue
                        if l[i][j]=="r":
                            if "b" in [l[i][j+1],l[i+1][j]]:
                                continue
                            else:
                                l[i][j]="b"
                                continue
                        
                    elif i==0 and j==len(l)-1:
                        if l[i][j]=="g":
                            if "b" in [l[i][j-1],l[i+1][j]] and "r" in [l[i][j-1],l[i+1][j]]:
                                continue
                            else:
                                l[i][j]="r"
                                continue
                        if l[i][j]=="r":
                            if "b" in [l[i][j-1],l[i+1][j]]:
                                continue
                            else:
                                l[i][j]="b"
                                continue
                        
                    elif i==len(l)-1 and j==0:
                        if l[i][j]=="g":
                            if "b" in [l[i][j+1],l[i-1][j]] and "r" in [l[i][j+1],l[i-1][j]]:
                                continue
                            else:
                                l[i][j]="r"
                                continue
                        if l[i][j]=="r":
                            if "b" in [l[i][j+1],l[i-1][j]]:
                                continue
                            else:
                                l[i][j]="b"
                                continue
                    elif i==len(l)-1 and j==len(l)-1:
                        if l[i][j]=="g":  
                            if "b" in [l[i][j-1],l[i-1][j]] and "r" in [l[i][j-1],l[i-1][j]]:
                                continue
                            else:
                                l[i][j]="r"
                                continue
                        if l[i][j]=="r":
                            if "b" in [l[i][j-1],l[i-1][j]]:
                                continue
                            else:
                                l[i][j]="b"
                                continue

            
                        


            elif (i,j) in us:
                y_l=[l[i+1][j],l[i][j+1],l[i][j-1]]
                if l[i][j]=="y":
                    
                    if "b" in y_l and "r" in y_l and "g" in y_l:
                        continue
                    else:
                        l[i][j]="g"
                        continue

                elif l[i][j]=="g":
                    if "b" in y_l and "r" in y_l:
                        continue
                    else:
                        l[i][j]="r"
                        continue
                elif l[i][j]=="r":
                    if "b" in y_l:
                        continue
                    else:
                        l[i][j]="b"
                        continue
            
            elif (i,j) in ds:
                y_l=[l[i-1][j],l[i][j+1],l[i][j-1]]
                if l[i][j]=="y":    
                    
                    if "b" in y_l and "r" in y_l and "g" in y_l:
                        continue
                    else:
                        l[i][j]="g" 
                elif l[i][j]=="g":
                    if "b" in y_l and "r" in y_l:
                        continue
                    else:
                        l[i][j]="r"
                        continue
                elif l[i][j]=="r":
                    if "b" in y_l:
                        continue
                    else:
                        l[i][j]="b"
                        continue

                

            elif (i,j) in ls:
                y_l=[l[i-1][j],l[i][j+1],l[i+1][j]]
                if l[i][j]=="y":    
                
                    if "b" in y_l and "r" in y_l and "g" in y_l:
                        continue
                    else:
                        l[i][j]="g" 
                        continue
                elif l[i][j]=="g":
                    if "b" in y_l and "r" in y_l:
                        continue
                    else:
                        l[i][j]="r"
                        continue
                elif l[i][j]=="r":
                    if "b" in y_l:
                        continue
                    else:
                        l[i][j]="b"
                        continue
                

            elif (i,j) in rs:
                y_l=[l[i-1][j],l[i][j-1],l[i+1][j]]                
                if l[i][j]=="y":    

                    if "b" in y_l and "r" in y_l and "g" in y_l:
                        continue
                    else:
                        l[i][j]="g"
                        continue
                elif l[i][j]=="g":
                    if "b" in y_l and "r" in y_l:
                        continue
                    else:
                        l[i][j]="r"
                        continue
                elif l[i][j]=="r":
                    if "b" in y_l:
                        continue
                    else:
                        l[i][j]="b"
                        continue

            else:
                c_l=[l[i-1][j],l[i+1][j],l[i][j+1],l[i][j-1]]
                if l[i][j]=="y":
                    
                    if "b" in c_l and "r" in c_l and "g" in c_l:
                        continue
                    else:
                        l[i][j]="g"
                        continue
                elif l[i][j]=="g":
                    if "b" in c_l and "r" in c_l:
                        continue
                    else:
                        l[i][j]="r"
                        continue
                elif l[i][j]=="r":
                    if "b" in c_l:
                        continue
                    else:
                        l[i][j]="b"
                        continue
                    
    return l