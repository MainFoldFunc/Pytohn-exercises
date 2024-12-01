def zdaniepalindrom(str_in):
    lst_in = list(str_in)
    lst_in = [x.strip(" ") for x in lst_in]
    l, r = 0, len(lst_in) -1
    while l <= r:
        if lst_in[l].lower() == lst_in[r].lower():
            l += 1
            r -= 1
        else: return print(False)
    return print(True)

zdaniepalindrom("Witam matiw")
zdaniepalindrom("Sport to zdrowie")