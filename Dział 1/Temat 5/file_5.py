from file_2 import NWD
from file_4 import NWW
def dodawanie_ulamkow(a, b, c, d):
    return print(format((a * (d/NWD(b, d))) + (c * (b/NWD(b, d))) / NWW(b, d), ".2f"))

dodawanie_ulamkow(3, 4, 5, 3)