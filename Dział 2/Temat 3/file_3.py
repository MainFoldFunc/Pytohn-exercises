def sortowanie_wstawianie(lst_in):
    for i in range(len(lst_in)):
        m = lst_in[i]
        j = i - 1
        while j >= 0 and lst_in[j] > m:
            lst_in[j + 1] = lst_in[j]
            j -= 1
        lst_in[j + 1] = m
        
    return lst_in
        
print(sortowanie_wstawianie([3, 4, 52, 1, 3, 4,22]))