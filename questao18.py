def impar_par_listas(l1, l2):
    for elemento1 in l1:
        if (elemento1 % 2 != 0):
            l3.append(elemento1)
            if len(l3) != 0:
                break
    
    for elemento2 in l2:
        if not (elemento2 % 2 != 0) :
            l3.append(elemento2)
    
    print(l3)
