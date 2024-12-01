def ileliter(str_in, litera):
    hash_map = {}
    for c in str_in:
        if c in hash_map:
            hash_map[c] += 1
        else:
            hash_map[c] = 1
    return print(hash_map[litera])

ileliter(input("Podaj słowo: "),input("Podaj literę: ") )