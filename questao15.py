#Exercício 15: Faça uma função que remova símbolos/pontuações especiais de uma string

print("Digite uma frase com caracteres especiais, como por exemplo: !,?,>,'.")
frase = input()

nova_frase = ''.join(filter(str.isalnum, frase))
print(nova_frase)
