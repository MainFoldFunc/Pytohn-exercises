def czy_w_zbiorze(lst_in, int_in):
    ret = False
    for element in lst_in:
        if element == int_in:
            ret = True
        
    return ret

print(czy_w_zbiorze([1,2,3,4], 5))