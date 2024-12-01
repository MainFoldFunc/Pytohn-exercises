def porownanie(int_in):
    list_int_in = list(str(int_in))
    if list_int_in[0] == list_int_in[-1]:
        return print("TAK")
    return print("NIE")
porownanie(919)
porownanie(981)