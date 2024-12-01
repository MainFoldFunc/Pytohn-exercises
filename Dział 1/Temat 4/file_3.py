from file_1 import pierwsza
def blizniacze(int_in):
    ret = []
    pomocnicza = 0
    x = 3
    while pomocnicza < int_in:
        if pierwsza(x) and pierwsza(x + 2):
            ret.append(x)
            ret.append(x + 2)
            ret.append(" ")
            pomocnicza += 1
        x += 2
        pomocnicza += 1 ### Dodaj tą linię gdy chcesz pary do stu a nie sto par. ###
    return print(ret)

blizniacze(100)
        
