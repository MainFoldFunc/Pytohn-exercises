def mini_maxi(lst_in):
    mini = int
    maxi = int
    pomocnicza = 0
    for element in lst_in:
        if pomocnicza == 0:
            mini = element
            maxi = element
        else:
            mini = min(mini, element)
            maxi = max(maxi, element)
        pomocnicza += 1
    return mini, maxi

print(mini_maxi([3,4,2,1,4,10]))