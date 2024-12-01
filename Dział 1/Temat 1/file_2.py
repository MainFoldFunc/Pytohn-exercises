def liczniki_calk(int_l):
    licznik_d = 0
    for i in range(int_l / 2):
        if int_l % i == 0:
            licznik_d += 1
            
    return licznik_d