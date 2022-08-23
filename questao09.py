def soma_produto(s1)
    for m in s1:
        if m.isdigit():
            soma = soma + int(m)
            produto = produto * int(m)

    print("Soma:", soma)
    print("Produto: ", produto)
