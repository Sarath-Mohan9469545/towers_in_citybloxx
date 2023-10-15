import random
import numpy as np

from pos_return import rpos,gpos,ypos
from check_pos import checkg,checkr,checky


def iterator(build_value,num_iter,city_size):    
    maxsvalue=0
    bestlist=[]
    for count in range(num_iter):
        l=[[0]*7 for i in range(7)]
        for i in range(1,6):
            for j in range(1,6):
                l[i][j]="b"
        while True:
            posy=ypos(l)
            if len(posy)!=0:
                y=random.choice(posy)
                l[y[0]][y[1]]="y"
            posg=gpos(l)
            if len(posg)!=0:
                g=random.choice(posg)
                l[g[0]][g[1]]="g"
            posr=rpos(l)
            if len(posr)!=0:
                r=random.choice(posr)
                l[r[0]][r[1]]="r"

            l=checkr(l)
            l=checkg(l)
            l=checky(l)
            if len(posr)==0 and len(posg)==0 and len(posy)==0:
                break
            
        

        unique, counts = np.unique(l, return_counts=True)
        s=0
        for i in range(len(unique)):
            s=s+build_value[unique[i]]*counts[i]
        if s>=maxsvalue:
            maxsvalue=s
            bestlist=l.copy()

    return bestlist,maxsvalue
