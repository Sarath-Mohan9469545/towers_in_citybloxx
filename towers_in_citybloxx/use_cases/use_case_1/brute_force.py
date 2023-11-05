import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))

from utils.args_parse import check_args

def main():
    d=check_args(sys.argv)
    print(d)
    size_of_city=sys.argv[1]
    print(size_of_city)
    print(isinstance(size_of_city,str))
    




if __name__=="__main__":
    main()