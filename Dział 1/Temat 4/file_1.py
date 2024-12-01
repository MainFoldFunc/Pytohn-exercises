def pierwsza (int_in):
    if int_in == 1:
        return False
    dzielniki = 2
    dzielnik = 2
    while dzielnik < ((int_in // 2) + 1):
        if int_in > 2 and int_in % 2 == 0:
            return False
        if int_in % dzielnik == 0:
            dzielniki += 1
        if dzielniki >= 3:
            return False
        dzielnik += 1
    return True
        
pierwsza(20)