def checkpos(l,us,ds,ls,rs):
    ijlist=[0,len(l)-1]
    wrong_pos=[]
    for i in range(len(l)):
        for j in range(len(l)):
            if i in ijlist and j in ijlist:
                if i==0 and j==0:
                    nl=[l[i+1][j],l[i][j+1]]

                elif i==0 and j==len(l)-1:
                    nl=[l[i][j-1],l[i+1][j]]
                
                elif i==len(l)-1 and j==0:
                    nl=[l[i][j+1],l[i-1][j]]

                else:
                    nl=[l[i][j-1],l[i-1][j]]


            elif (i,j) in us:
                nl=[l[i][j-1],l[i][j+1],l[i+1][j]]

            elif (i,j) in ds:
                nl=[l[i][j+1],l[i][j-1],l[i-1][j]]

            elif (i,j) in ls:
                nl=[l[i+1][j],l[i-1][j],l[i][j+1]]

            elif (i,j) in rs:
                nl=[l[i+1][j],l[i-1][j],l[i][j-1]]

            else:
                nl=[l[i+1][j],l[i-1][j],l[i][j-1],l[i][j+1]]


            if l[i][j]=="y" and "b" in nl and "r" in nl and "g" in nl:
                    continue
            elif l[i][j]=="y":
                wrong_pos.append((i,j))
                continue
            
            if l[i][j]=="g" and "b" in nl and "r" in nl:
                continue
            elif l[i][j]=="g":
                wrong_pos.append((i,j))
                continue
            
            if l[i][j]=="r" and "b" in nl:
                continue
            elif l[i][j]=="r":
                wrong_pos.append((i,j))
                continue

    return wrong_pos