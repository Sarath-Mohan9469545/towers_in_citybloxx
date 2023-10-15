
def rpos(l):
    posr=[]
    for i in range(1,6):
        for j in range(1,6):
            if l[i+1][j]=="b" or l[i-1][j]=="b" or l[i][j+1]=="b" or l[i][j-1]=="b":
                if l[i][j]=="b":
                    posr.append((i,j))
    return posr


def gpos(l):
    posg=[]
    for i in range(1,6):
        for j in range(1,6):
            neighbours=[l[i-1][j],l[i+1][j],l[i][j-1],l[i][j+1]]
            if "r" in neighbours and "b" in neighbours and l[i][j]!="g" and l[i][j]!="y":
                posg.append((i,j))
    return posg


def ypos(l):
    posy=[]
    for i in range(1,6):
        for j in range(1,6):
            neighbours=[l[i-1][j],l[i+1][j],l[i][j-1],l[i][j+1]]
            if "r" in neighbours and "g" in neighbours and "b" in neighbours and l[i][j]!="y":
                posy.append((i,j))
    return posy