print("digite uma frase:")

def separar_frase(palavras):
    lista_de_palavras = palavras.split(' ')
    return lista_de_palavras

def juntar_palavras(lista_de_palavras):
    palavras = '-'.join(lista_de_palavras)
    return palavras

if __name__ == '__main__':
    palavras = input()

    frase = separar_frase(palavras)

    nova_frase = juntar_palavras(frase)
    print(nova_frase)

for palavras in frase:
    print(palavras)
