from file_2 import NWD
def skrucenie_ulamka(l, m):
    dzielnik = NWD(l, m)
    return print(int(l / dzielnik), int(m / dzielnik))

skrucenie_ulamka(10, 30)