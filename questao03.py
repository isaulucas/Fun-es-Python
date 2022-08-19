#Exercício 3: Dadas duas strings, s1 e s2, escreva um programa para retornar uma nova string feita de primeiro, meio e último caracteres de s1 e s2.

print("Digite uma palavra:")
s1 = input()
print("Digite outra palavra:")
s2 = input()
print("\nEstas sao suas palavras: ", s1, "e", s2)
tamanho_da_s1 = len(s1)
metade_da_s1 = (tamanho_da_s1 // 2)
tamanho_da_s2 = len(s2)
metade_da_s2 = (tamanho_da_s2 // 2)
s3 = s1[0] + s2[0] + s1[metade_da_s1] + s2[metade_da_s2] + s1[-1] + s2[-1]
print("\nE esta eh uma nova palavra, formada pela primeira letra, a letra do meio e a ultima letra das duas palavras que vc digitou: ", s3)
