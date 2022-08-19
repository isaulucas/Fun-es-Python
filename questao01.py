#Exercício 1: Escreva uma função para criar uma nova string feita do primeiro, do meio e do último caractere de uma string de entrada.

print("Digite uma palavra:")
palavra = input()
print("esta eh sua palavra:", palavra)
tamanho_da_palavra = len(palavra)
metade_da_palavra = (tamanho_da_palavra//2)
nova_palavra = palavra[0] + palavra[metade_da_palavra] + palavra[-1]
print("esta eh sua palavra apenas com a primeira letra, a letra do meio e a letra final:", nova_palavra)
