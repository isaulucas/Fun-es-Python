def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    tuple(l)
    print(l)
    print(min(l))
    print(max(l))
