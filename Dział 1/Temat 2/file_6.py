def czy_trojkat(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return print(True)
    return print(False)
czy_trojkat(100,100,1)