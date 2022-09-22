# Challenge solution by Jonas

from random import randint as rd

mtz = [[rd(0, 100) for a in range(10)] for b in range(10)] # Cria uma matriz 10x10 com numeros aleatórios de 0 à 100
# Imprime a matriz formatada em 10x10 
for i in mtz:
  for j in i:
    print(j, end=" ")
  print()

maior = x = y = 0 # cria 3 variáveis com o valor de 0
# lê a matriz e pega o maior valor e sua posição no eixo x e y
for i in range(len(mtz)):
  for j in range(len(mtz)):
    if mtz[i][j] > maior:
      maior, x, y = mtz[i][j], i, j
print(f"{'-'*55}\nO maior valor é {maior}, e se encontra na posição x {x}, y {y} ")
