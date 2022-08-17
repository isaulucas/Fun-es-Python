s = "OLA EU ESTUDO PYTHON A 3 MESES , 7 DIAS, 2 horas"
resultado = ''.join(filter(lambda i: i if i.isdigit() else None, s))
print(resultado)
