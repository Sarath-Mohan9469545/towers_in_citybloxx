def c_s(args_list,city_size):
    cs=city_size
    if args_list[1].isdigit():
        if 3<=eval(args_list[1]):
            cs=eval(args_list[1])
        else:
            raise Exception("City size should be greater than two.")
    else:
        raise Exception("City size should be a number greater than two.")
    return cs

def i_c(args_list,iterations):
    it=iterations
    if args_list[2].isdigit():
        if 1<=eval(args_list[2]):
            it=eval(args_list[2])
        else:
            raise Exception("Number of iterations should be greater than one.")
    else:
        raise Exception("Number of iterations should be a number greater than zero.")
    return it



def check_args(args_list):

    if args_list[0][-14:]=="brute_force.py":
        city_size=5
        iterations=10000
    if len(args_list)==2:
        city_size=c_s(args_list,city_size)

    elif len(args_list)==3:
        city_size=c_s(args_list,city_size)
        iterations=i_c(args_list,iterations)

    elif len(args_list)==0:
        raise Exception("Only city size and number of iterations are allowed as inputs.")

    return city_size,iterations



                        






        
