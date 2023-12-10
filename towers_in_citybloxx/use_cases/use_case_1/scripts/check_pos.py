def check_pos(l,us,ds,ls,rs):
    for i in range(len(l)):
        for j in range(len(l)):
            ijlist=[0,len(l)-1]

            if i in ijlist and j in ijlist:
                if l[i][j]=="y":
                    l[i][j]=="g"
                else:
                    if i==0 and j==0:
                        if l[i][j]=="g" and "b" in [l[i][j+1],l[i+1][j]] and "r" in [l[i][j+1],l[i+1][j]]:
                            continue
                        else:
                            l[i][j]=="r"
                        


            elif (i,j) in us:
                
                if l[i][j]=="y":
                    y_l=[l[i+1][j],l[i][j+1],l[i][j-1]]
                    if "b" in y_l and "r" in y_l and "g" in y_l:
                        continue
                    else:
                        l[i][j]=="g"
            
            elif (i,j) in ds:
                if l[i][j]=="y":    
                    y_l=[l[i-1][j],l[i][j+1],l[i][j-1]]
                    if "b" in y_l and "r" in y_l and "g" in y_l:
                        continue
                    else:
                        l[i][j]=="g" 

            elif (i,j) in ls:
                if l[i][j]=="y":    
                    y_l=[l[i-1][j],l[i][j+1],l[i+1][j]]
                    if "b" in y_l and "r" in y_l and "g" in y_l:
                        continue
                    else:
                        l[i][j]=="g" 
            elif (i,j) in rs:
                if l[i][j]=="y":    
                    y_l=[l[i-1][j],l[i][j-1],l[i+1][j]]
                    if "b" in y_l and "r" in y_l and "g" in y_l:
                        continue
                    else:
                        l[i][j]=="g"

            else:
                if l[i][j]=="y":
                    c_l=[l[i-1][j],l[i+1][j],l[i][j+1],l[i][j-1]]
                    if "b" in c_l and "r" in c_l and "g" in c_l:
                        continue
                    else:
                        l[i][j]=="g"
                    
    