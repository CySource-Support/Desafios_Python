# Challenge Solution by Jonas
# Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.

num = int(input("Informe um número: "))
cont = 0
while cont <= 10:
  print(f"{num} X {cont} = {num * cont} ")
  cont += 1
