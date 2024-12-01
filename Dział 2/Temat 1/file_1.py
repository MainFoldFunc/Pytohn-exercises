def liczymy_litery(str_in):
    hash_map = {}
    for element in str_in:
        if element in hash_map and element != " ":
            hash_map[element] += 1
        elif element not in hash_map and element != " ":
            hash_map[element] = 1
            
    return max(hash_map) ### Można usunąć max wtedy działa normalnie ###
with open("file_1.txt", "r") as file:
    file_r = file.read()
    print(liczymy_litery(file_r))