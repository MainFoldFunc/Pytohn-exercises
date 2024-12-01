def sortowanie_wybieranie(lst_in):
    for i in range(len(lst_in)):
        min_index = i
        
        for j in range(i + 1, len(lst_in)):  
            if lst_in[j] < lst_in[min_index]:
                min_index = j

        lst_in[i], lst_in[min_index] = lst_in[min_index], lst_in[i]
        
    return lst_in

        
print(sortowanie_wybieranie([1,4,3,2,5,3,2,1]))