def przestawienie(string_in, klucz):
    str_in = list(string_in)
    ret = ""

    while len(str_in) % klucz != 0:
        str_in.append("X") 

    for i in range(klucz):
        for j in range(len(str_in) // klucz):
            ret += str_in[j * klucz + i] 
    
    return ret

def od_przestawienie(str_in):
    pass
        
print("Siema")
print(przestawienie("Siema", 4))
