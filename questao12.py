#Exercício 12: Escreva um programa para encontrar a última posição de uma substring “ Emma ” em uma determinada string.

print("Conte uma pequena estoria sobre uma menina chamada Emma.")

estoria = input()
tamanho_string = len(estoria)
print("Essa pequena estoria tem", tamanho_string, "substrings.")

print("Qual a ultima posicao em que Emma aparece nessa string? Ops, estoria?")
index = estoria.rfind("Emma")
print("Na posicao", index)
