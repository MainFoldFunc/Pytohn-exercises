def binary_search(lst_in, int_in):
    l, r = 0, len(lst_in) - 1
    while l <= r:
        m = (l + r) // 2
        if lst_in[m] > int_in:
            r = m - 1
        elif lst_in[m] < int_in:
            l = m + 1
        else:
            return True 
    return False


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))