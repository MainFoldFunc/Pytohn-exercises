def bin_do_dziesietna(int_in):
    lst_in = list(str(int_in))
    dziesietny = 0
    pomocnicza = len(lst_in) - 1
    for element in lst_in:
        dziesietny += int(element) * (2 ** pomocnicza)
        pomocnicza -= 1
    return print(dziesietny)

bin_do_dziesietna(101)