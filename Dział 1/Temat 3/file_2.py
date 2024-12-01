def palindrom (str_in):
    lst_in = list(str_in)
    l, r = 0, len(lst_in) -1
    while l <= r:
        if lst_in[l].lower() == lst_in[r].lower():
            l += 1
            r -= 1
        else: return False
        
    return True
        