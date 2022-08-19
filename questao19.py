# Exercício 19: Escreva um programa para remover o item presente no índice 4 e adicioná-lo na 2ª posição e no final da lista.

print("Vamos criar uma lista? Digite a quantidade de palavras voce quer na sua lista.")
lista = []
quant_palavras = int(input())

contador = 0
while contador < quant_palavras:
    lista.append(input("Insira a palavra:"))
    contador = contador + 1

print("Essa eh sua lista: ", lista)

palavra_indice_quatro = lista[4]

del lista[4]
lista.insert(1, palavra_indice_quatro)
lista.append(palavra_indice_quatro)

print("\nEssa eh sua nova lista: ", lista)
