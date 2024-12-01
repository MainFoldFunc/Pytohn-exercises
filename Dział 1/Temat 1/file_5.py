def sum_cyfr(int_in):
    str_int_in = str(int_in)
    list_int = []
    for element in str_int_in:
        list_int.append(element)
    sum = 0
    for element in list_int:
        sum += int(element)
    return print(sum)

sum_cyfr(911)