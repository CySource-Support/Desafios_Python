#  Challenge Solution by Jonas
#  Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre o mais barato.

# modo simplificado
#print(min(list(map(float, input("Informe o valor de 3 produtos: ").split(" ")))))

# modo mais legivel
preco, cont = [], 0
while cont < 3: # loop para pegar os 3 preços
  preco.append(float(input("Informe o valor do produtos: R$ ")))
  cont += 1

# comparar o menor valor
menor = preco[0]
for i in preco:
  if menor > i:
    menor = i

print(f"O menor preço é R$ {menor}.")
