import random
import numpy as np
from tqdm import tqdm

from .pos_return import reassign

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
            #l[i][j]=random.choice(["b","r","g","y"])
            if i==0 and 0<j<len(l)-1:
                us.append((i,j))
            if i==len(l)-1 and 0<j<len(l)-1:
                ds.append((i,j))
            if j==0 and 0<i<len(l)-1:
                ls.append((i,j))
            if j==len(l)-1 and 0<i<len(l)-1:
                rs.append((i,j))


    prev_value=0
    for _ in tqdm(range(num_iter)):
        l=[[0]*city_size for i in range(city_size)]
        for i in range(city_size):
            for j in range(city_size):
                l[i][j]=random.choice(["b","r","g","y"])
        iter_n=0
        while True:
            wrong_pos=checkpos(l,us,ds,ls,rs)
            if len(wrong_pos)==0:
                break
            l=reassign(wrong_pos,l)
            
        value=0

        for i in range(city_size):
            for j in range(city_size):
                value=build_value[l[i][j]]+value
        
        if value>prev_value:
            best_list=l.copy()
            prev_value=value


    print(f"Score of city is {value}")
    return best_list