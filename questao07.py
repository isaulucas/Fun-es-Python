def teste_de_balanceamento(s1, s2):

    teste = True
    for char in s1:
        if char in s2:
            continue
        else:
            teste = False
    return teste
