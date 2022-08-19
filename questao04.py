#Exercício 4: Dada uma string que contém uma combinação de letras maiúsculas e minúsculas.
#Escreva uma função para organizar os caracteres de uma string de forma que todas as letras minúsculas venham primeiro.

print("Digite uma frase ou palavra:")

entrada = input()
print("Voce digitou isso: " + str(entrada))
res1 = [char for char in entrada if char.islower()]
res2 = [char for char in entrada if char.isupper()]
saida = ''.join(res1 + res2)
print( "Ordenando de forma que as minusculas sejam exibidas primeiro: " + saida)
