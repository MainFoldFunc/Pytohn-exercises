from file_2 import palindrom
def palindrom_wzdaniu(str_in):
    ret = []
    while len(str_in) > 0:
        i = str_in.index(" ")
        if i > 0:
            zdanie = str_in[:i]
            zdanie_pre = str_in[:i + 1]
            if palindrom(zdanie):
                ret.append(zdanie)
            str_in = str_in.replace(zdanie_pre, "")
    return print(ret)
            
palindrom_wzdaniu("Witam serdecznie na kajak ")
            