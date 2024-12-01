import random
def losuj(lst_in):
    return lst_in[random.randint(0, len(lst_in) -1)]

def main():
    lst = [1,2,3,4]
    for element in range(int(input(f"Ile elementów z listy chcesz wylosować max to  {len(lst)}: "))):
        print(losuj(lst))
        
main()