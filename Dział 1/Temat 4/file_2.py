def czynnik_pierwsz(int_in):
    or_int = int_in
    ret = []
    dzielnik = 2
    while dzielnik ** 2 <= int_in:
        if int_in % dzielnik == 0:
            ret.append(str(dzielnik))
            ret.append("*")
            int_in //= dzielnik 
        else:
            dzielnik += 1
    if int_in > 1: 
        ret.append(str(int_in))
        
    ret_str = ""
    for element in ret:
        ret_str += element
    print(f"{or_int} = {ret_str}")
    
czynnik_pierwsz(90)
