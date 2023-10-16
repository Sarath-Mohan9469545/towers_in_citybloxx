def check_args(args_list):
    if args_list[0]=="brute_force.py" and len(args_list)<=2:
        return "Yes"
    elif len(args_list)>2:
        raise Exception("Only city size is accepted as a parameter fo brute force method.")
        
