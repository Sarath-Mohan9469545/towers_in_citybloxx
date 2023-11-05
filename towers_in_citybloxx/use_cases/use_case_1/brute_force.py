import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))

from utils.args_parse import check_args

def main():
    city_size,iterations=check_args(sys.argv)
    print(city_size)
    print(iterations)
    




if __name__=="__main__":
    main()