def vineger(str_in, list_in):
    ret = ""
    for element, przesuniecie in zip(str_in, list_in):
        ret += chr(int(ord(element) + przesuniecie))
    return ret

def deszyfr_vineger(str_in, list_in):
    ret = ""
    for element, przesuniecie in zip(str_in, list_in):
        ret += chr(int(ord(element) - przesuniecie))
        
    return ret


print(vineger("Cześć", [1, 2, 3, 4, 5]))
print(deszyfr_vineger(vineger("Cześć", [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]))