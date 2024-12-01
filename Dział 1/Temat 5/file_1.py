# Nie działa może kiedy naprawie #
def NWD (a, b):
    while a != b and a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return print(b)
NWD(10, 30)