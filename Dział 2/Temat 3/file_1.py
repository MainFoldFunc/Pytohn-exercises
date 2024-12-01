def buble_sort(lst_in):
    for i in range(len(lst_in)):
        for j in range(len(lst_in) - i - 1):
            if lst_in[j] > lst_in[j + 1]:
                lst_in[j], lst_in[j + 1] = lst_in[j + 1], lst_in[j]
    return lst_in

print(buble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 4, 5, 6, 4, 2]))