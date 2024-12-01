def czy_anagram(str_in, str_in_2):
    lst_1 = list(str_in)
    lst_2 = list(str_in_2)
    lst_1.sort()
    lst_2.sort()
    if lst_2 == lst_1:
        return True
    return False

print(czy_anagram("kajak", "kajak"))
print(czy_anagram("kajak", "kaja"))