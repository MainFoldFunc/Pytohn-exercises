from file_2 import NWD
from file_4 import NWW
def mnozenie_ulamkow(a, b, c, d):
    return print(format((a/NWD(a, d) * (c/NWD(c,b))) / (b/NWD(c, b) * (d/NWD(a,d))), ".2f"))

mnozenie_ulamkow(10, 5, 4, 3)