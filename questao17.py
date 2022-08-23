def checar_string(string):
    t_numero = False
    t_letra = False

    for i in string:

        if i.isalpha():
            t_letra = True

        if i.isdigit():
            t_numero = True

    return t_letra and t_numero
