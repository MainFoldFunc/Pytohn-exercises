def dziesietne_na_bin(int_in):
    out = ""
    binarna = []
    if int_in > 0:
        while int_in > 0:
            binarna.append(str(int_in % 2)) 
            int_in //= 2
        if len(binarna) < 8:
            while len(binarna) != 8:
                binarna.append(0)
        binarna_odwirot = binarna[::-1] 
        for element in binarna_odwirot:
            out += str(element)
        return print(out)
    else:
        while int_in + (-2 * int_in) > 0:
            binarna.append(str(int_in % 2))
            int_in //= 2
        if len(binarna) < 8:
            while len(binarna) != 8:
                binarna.append(1)
        binarna_odwirot = binarna[::-1] 
        for element in binarna_odwirot:
            out += str(element)
        return print(out)

dziesietne_na_bin(100)