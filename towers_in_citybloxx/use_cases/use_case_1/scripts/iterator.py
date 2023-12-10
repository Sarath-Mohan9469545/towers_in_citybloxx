import random
import numpy as np
from tqdm import tqdm

from .pos_return import rpos,gpos,ypos

from .check_pos import checkpos


def iterator(num_iter,city_size,build_value={"b":70,"r":250,"g":550,"y":1000,"0":0}):    
    maxsvalue=0
    bestlist=[]
    us=[]
    ds=[]
    ls=[]
    rs=[]
    l=[[0]*city_size for i in range(city_size)]
    for i in range(city_size):
        for j in range(city_size):
            l[i][j]=random.choice(["b","r","g","y"])
            if i==0 and 0<j<len(l)-1:
                us.append((i,j))
            if i==len(l)-1 and 0<j<len(l)-1:
                ds.append((i,j))
            if j==0 and 0<i<len(l)-1:
                ls.append((i,j))
            if j==len(l)-1 and 0<i<len(l)-1:
                rs.append((i,j))


    
    for _ in tqdm(range(num_iter)):
        checkpos(l,us,ds,ls,rs)






    return bestlist,maxsvalue
