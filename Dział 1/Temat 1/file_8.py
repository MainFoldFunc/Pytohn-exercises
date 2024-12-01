def najminejsza_cyfra(int_in):
    str_int_in = str(int_in)
    list_int = []
    for element in str_int_in:
        list_int.append(element)
    return print(min(list_int))

najminejsza_cyfra(98731)