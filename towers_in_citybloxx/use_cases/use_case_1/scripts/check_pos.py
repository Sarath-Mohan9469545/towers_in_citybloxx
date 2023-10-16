def checkr(l):
    for i in range(1,6):
        for j in range(1,6):
            if l[i+1][j]=="b" or l[i-1][j]=="b" or l[i][j+1]=="b" or l[i][j-1]=="b":
                continue
            elif l[i][j]=="r":
                l[i][j]="b"
    return l

def checkg(l):
    for i in range(1,6):
        for j in range(1,6):
            neighbours=[l[i-1][j],l[i+1][j],l[i][j-1],l[i][j+1]]
            if "r" in neighbours and "b" in neighbours:
                continue
            elif l[i][j]=="g":
                if "b" in neighbours:
                    l[i][j]="r"
                else:
                    l[i][j]="b"
    return l
    
def checky(l):
    for i in range(1,6):
        for j in range(1,6):
            neighbours=[l[i-1][j],l[i+1][j],l[i][j-1],l[i][j+1]]
            if "r" in neighbours and "g" in neighbours and "b" in neighbours:
                continue
            elif l[i][j]=="y":
                if "r" in neighbours and "b" in neighbours:
                    l[i][j]="g"
                elif "b" in neighbours:
                    l[i][j]="r"
                else:
                    l[i][j]="b"
    return l