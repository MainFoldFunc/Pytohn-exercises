def nacyfry(int_in):
    str_int_in = str(int_in)
    list_int = []
    for element in str_int_in:
        list_int.append(element)
    pomocnicza = 1
    for element in list_int:
        print(f"Cyfra numer {pomocnicza} to: {element}")
        pomocnicza += 1
        
nacyfry(984)