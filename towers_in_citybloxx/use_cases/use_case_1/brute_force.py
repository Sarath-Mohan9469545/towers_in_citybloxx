import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))

from utils.args_parse import check_args
from scripts.iterator import iterator
from utils.city_disp import plot_city

def main():
    city_size,iterations=check_args(sys.argv)
    bestlist=iterator(iterations,city_size,build_value={"b":70,"r":250,"g":550,"y":1000})

    plot_city(bestlist)
    
    #print(bestlist)
    




if __name__=="__main__":
    main()