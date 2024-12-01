from file_1 import cezar, reszyfr_cezar
with open("file_2.txt", "r") as file_r:
    file = file_r.read()
    print(cezar(file, 2))
    print(reszyfr_cezar(cezar(file, 2), 2))
    file_r.close()