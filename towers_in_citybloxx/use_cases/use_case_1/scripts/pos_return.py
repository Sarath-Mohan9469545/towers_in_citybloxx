def reassign(wrong_pos,l):
    c=["b","r","g","y"]
    for p in wrong_pos:
        i=p[0]
        j=p[1]
        l[i][j]=c[c.index(l[i][j])-1]

    return l