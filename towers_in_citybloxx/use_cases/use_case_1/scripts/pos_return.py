def reassign(l,us,ds,ls,rs):
    for i in range(len(l)):
        for j in range(len(l)):
            ijlist=[0,len(l)-1]

            if i in ijlist and j in ijlist:
                if i==0 and j==0:
                    cl=[l[i][j+1],l[i+1][j]]
                elif i==0 and j==len(l)-1:
                    cl=[l[i][j-1],l[i+1][j]]
                elif i==len(l)-1 and j==0:
                    cl=[l[i][j+1],l[i-1][j]]
                elif i==len(l)-1 and j==len(l)-1:
                    cl=[l[i][j-1],l[i-1][j]]
            
            elif (i,j) in us:
                cl=[l[i+1][j],l[i][j+1],l[i][j-1]]
            elif (i,j) in ds:
                cl=[l[i-1][j],l[i][j+1],l[i][j-1]]
            elif (i,j) in ls:
                cl=[l[i-1][j],l[i][j+1],l[i+1][j]]
            elif (i,j) in rs:
                cl=[l[i-1][j],l[i][j-1],l[i+1][j]]
            else:
                cl=[l[i-1][j],l[i][j-1],l[i+1][j],l[i][j+1]]
            
            flag=0
            if l[i][j]=="g" and "g" in cl and "r" in cl and "b" in cl:
                l[i][j]="y"
                flag=1
            elif l[i][j]=="r" and "g" in cl and "r" in cl and "b" in cl:
                l[i][j]="y"
                flag=1
            elif l[i][j]=="r" and "r" in cl and "b" in cl:
                l[i][j]="g"
                flag=1
            elif l[i][j]=="b" and "g" in cl and "r" in cl and "b" in cl:
                l[i][j]="y"
                flag=1
            elif l[i][j]=="b" and "r" in cl and "b" in cl:
                l[i][j]="g"
                flag=1
            elif l[i][j]=="b" and "b" in cl:
                l[i][j]="r"
                flag=1
                
    return l,flag   


