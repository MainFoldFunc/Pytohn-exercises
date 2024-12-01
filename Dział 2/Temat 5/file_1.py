def podciag_niemalejacy(lst_in):
    max_dl = 1
    akt_dl = 1
    max_pod = 0
    akt_pod = 0
    for i in lst_in:
        if i >= i - 1:
            akt_dl += 1
            max_dl = max(max_dl, akt_dl)
            max_pod = max(max_pod, akt_pod)
        else:
            akt_dl = 1
            akt_pod = i
    return max_dl - 1, max_pod

print(podciag_niemalejacy([1, 2, 3, 4, 5, 6,7 ,8 ,9]))
print(podciag_niemalejacy([1, 2, 3, 4, 5, 6,7 ,8 ,9]))
print(podciag_niemalejacy([1, 2, 3, 4, 5, 6,7 ,8 ,9]))
# * print(podciag_niemalejacy([1, 2, 3, 4, 5, 6,7 ,8 ,9]))
# TODO
            