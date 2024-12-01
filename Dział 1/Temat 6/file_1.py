def cezar(str_in, klucz):
    list_in = list(str_in)
    klucz_poprawny = klucz % 26
    ret = ""
    for element in list_in:
        ret += chr(int(ord(element) + klucz_poprawny))
    return ret


def reszyfr_cezar(str_in, klucz):
    list_in = list(str_in)
    klucz_poprawny = klucz % 26
    ret = ""
    for element in list_in:
        ret += chr(int(ord(element) - klucz_poprawny))
    return ret
