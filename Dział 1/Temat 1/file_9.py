def cyfry_parzyste(int_in):
    str_int_in = str(int_in)
    list_int = []
    for element in str_int_in:
        list_int.append(element)
    for element in list_int:
        if int(element) % 2 != 0:
            return print(False)
    return print(True)
cyfry_parzyste(888)
cyfry_parzyste(887)
        